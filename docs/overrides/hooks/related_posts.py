import os
import re
import math
from collections import Counter, defaultdict
from textwrap import dedent
import yaml
from urllib.parse import urljoin

# 存储所有文章的信息和索引
article_index = {}
category_index = defaultdict(list)
keyword_index = defaultdict(set)
# 全局词频（用于 IDF 计算，纯标准库实现 TF-IDF）
global_doc_freq = defaultdict(int)   # 词 -> 出现该词的文章数
total_docs = 0

# 配置：需要索引的目录
INDEXED_DIRECTORIES = ['blog/', 'develop/']  

# 配置：排除推荐的页面列表（支持精确匹配和模式匹配）
EXCLUDED_PAGES = {
    # 精确路径匹配
    'blog/index.md',
    'develop/index.md',
    # 可以添加更多排除的页面
    # 'blog/special-page.md',
}

# 配置：排除推荐的页面模式（支持通配符）
EXCLUDED_PATTERNS = [
    r'.*\/index\.md$',  # 排除所有 index.md 文件
    r'.*\/archive\.md$',  # 排除所有 archive.md 文件
    r'blog\/posts?\/.*',  # 排除 blog/post/ 和 blog/posts/ 目录下的所有文章
    # 可以添加更多模式
    # r'blog\/draft\/.*',  # 排除草稿目录
]

# 配置：相似度阈值和权重（各维度已归一化到 [0,1]，权重之和=1 时即真实占比）
SIMILARITY_CONFIG = {
    'min_threshold': 0.05,  # 最低相似度阈值（归一化后尺度更小）
    'weights': {
        'keywords': 0.35,    # 关键词(TF-IDF)相似度
        'tags': 0.30,        # 标签相似度
        'categories': 0.20,  # 分类相似度
        'path': 0.10,        # 路径分类相似度
        'source_dir': 0.05   # 源目录相似度
    },
    'title_similarity': 0.20,  # 标题相似度权重（叠加项，独立于上面归一化维度）
    'mmr_lambda': 0.7         # MMR 多样性参数：越高越偏相关性，越低越偏多样性
}

def is_page_excluded(file_path):
    """检查页面是否应该排除推荐"""
    # 精确匹配检查
    if file_path in EXCLUDED_PAGES:
        return True
    
    # 模式匹配检查
    for pattern in EXCLUDED_PATTERNS:
        if re.match(pattern, file_path):
            return True
    
    return False

def should_index_file(file_path):
    """检查文件是否应该被索引"""
    if not file_path.endswith('.md'):
        return False
    
    # 先检查是否被排除
    if is_page_excluded(file_path):
        return False
    
    # 检查是否在指定目录下
    for directory in INDEXED_DIRECTORIES:
        if file_path.startswith(directory):
            return True
    
    return False

# 扩展停用词列表（包含中英文）
STOPWORDS = {
    # 英文停用词
    'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'of', 'and', 'or', 'is', 'are', 'was', 'were',
    'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
    'this', 'that', 'these', 'those', 'with', 'from', 'by', 'as', 'can', 'but', 'not', 'if', 'it',
    'they', 'them', 'their', 'you', 'your', 'we', 'our', 'my', 'me', 'i', 'he', 'she', 'him', 'her',
    # 常见无意义词
    'about', 'above', 'after', 'again', 'all', 'also', 'any', 'because', 'before', 'between',
    'both', 'each', 'few', 'first', 'get', 'how', 'into', 'just', 'last', 'made', 'make', 'may',
    'most', 'new', 'now', 'old', 'only', 'other', 'over', 'said', 'same', 'see', 'some', 'such',
    'take', 'than', 'then', 'time', 'two', 'use', 'very', 'way', 'well', 'where', 'when', 'which',
    'while', 'who', 'why', 'work', 'world', 'year', 'years',
    # 中文停用词（单字 + 常见词）
    '的', '了', '和', '是', '就', '都', '而', '及', '与', '这', '那', '有', '在', '中', '为', '对', '等',
    '能', '会', '可以', '没有', '什么', '一个', '自己', '这个', '那个', '这些', '那些', '如果', '因为', '所以',
    '我', '你', '他', '她', '它', '我们', '你们', '他们', '它们', '也', '还', '又', '要', '把', '被', '让',
    '啊', '吧', '呢', '吗', '呀', '嘛', '其', '之', '于', '将', '已', '并', '或', '即', '便', '则', '但',
}

def clean_markdown(text):
    """移除 markdown 中的噪声（front matter / 代码块 / HTML / 链接 / 标题符）"""
    text = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL | re.MULTILINE)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)        # 代码块
    text = re.sub(r'`[^`]*`', '', text)                            # 行内代码
    text = re.sub(r'<.*?>', '', text)                             # HTML 标签
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)                   # 图片
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)                    # 链接
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)         # 标题标记
    return text

def tokenize(text):
    """纯标准库分词：英文/数字按词，中文用 2~4 字 n-gram 滑窗"""
    tokens = []
    # 英文/数字词（保留技术词如 docker, k8s, api2）
    tokens += re.findall(r'[a-zA-Z][a-zA-Z0-9+#.\-]*', text.lower())
    # 中文连续片段，做 2~4 字 n-gram
    for seg in re.findall(r'[\u4e00-\u9fff]+', text):
        n = len(seg)
        for k in (2, 3, 4):
            if k > n:
                continue
            for i in range(n - k + 1):
                tokens.append(seg[i:i + k])
    return tokens

def extract_keywords(content, title, top_k=15):
    """提取关键词：中文 n-gram 分词 + TF-IDF 加权（纯标准库，无需 jieba）"""
    body = clean_markdown(content)
    title_text = clean_markdown(title)

    # 标题词权重 ×4
    raw = tokenize(body) + tokenize(title_text) * 4

    # 过滤停用词 / 单字中文 / 纯数字 / 过短
    def keep(w):
        if w in STOPWORDS:
            return False
        if w.isdigit():
            return False
        # 中文必须是多字（n-gram 已满足），英文至少 2 字符
        if re.fullmatch(r'[a-zA-Z0-9+#.\-]+', w) and len(w) < 2:
            return False
        return True

    words = [w for w in raw if keep(w)]

    # TF：词频
    tf = Counter(words)

    # IDF：基于全局文档频率（在 on_files 阶段统计）
    def idf(term):
        df = global_doc_freq.get(term, 0)
        if df == 0:
            return 0.0
        return math.log((total_docs + 1) / (df + 1)) + 1.0  # 平滑 IDF

    # TF-IDF 排序
    scored = [(term, tf[term] * idf(term)) for term in tf]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]

def extract_metadata(content):
    """提取文章元数据，支持YAML front matter"""
    metadata = {
        'title': "未命名",
        'description': "",
        'tags': [],
        'categories': [],
        'disable_related': False  # 新增：是否禁用相关推荐
    }
    
    # 尝试解析YAML front matter
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if yaml_match:
        try:
            yaml_content = yaml_match.group(1)
            yaml_data = yaml.safe_load(yaml_content)
            if yaml_data:
                metadata['title'] = str(yaml_data.get('title', '未命名')).strip('"\'')
                metadata['description'] = str(yaml_data.get('description', '')).strip('"\'')
                metadata['disable_related'] = yaml_data.get('disable_related', False)
                
                # 处理tags
                tags = yaml_data.get('tags', [])
                if isinstance(tags, list):
                    metadata['tags'] = [str(tag).strip() for tag in tags]
                elif isinstance(tags, str):
                    metadata['tags'] = [tag.strip() for tag in tags.split(',') if tag.strip()]
                
                # 处理categories
                categories = yaml_data.get('categories', [])
                if isinstance(categories, list):
                    metadata['categories'] = [str(cat).strip() for cat in categories]
                elif isinstance(categories, str):
                    metadata['categories'] = [cat.strip() for cat in categories.split(',') if cat.strip()]
        except yaml.YAMLError:
            pass  # 如果YAML解析失败，使用默认值
    
    # 如果YAML解析失败，回退到正则表达式
    if metadata['title'] == "未命名":
        title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip('"\'')
    
    return metadata

def get_category_from_path(file_path):
    """从文件路径提取分类"""
    parts = file_path.split('/')
    if len(parts) > 2:
        return parts[1]  # blog/category/file.md 或 develop/category/file.md格式
    elif len(parts) > 1:
        return parts[0]  # blog 或 develop
    return "未分类"

def on_files(files, config):
    """预处理所有文章，建立索引"""
    global article_index, category_index, keyword_index, global_doc_freq, total_docs
    
    # 清空索引
    article_index.clear()
    category_index.clear()
    keyword_index.clear()
    global_doc_freq.clear()
    total_docs = 0
    
    processed_count = 0
    excluded_count = 0
    
    # 第一遍：建索引
    for file in files:
        if should_index_file(file.src_path):
            try:
                with open(file.abs_src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # 提取元数据
                    metadata = extract_metadata(content)
                    
                    # 检查是否禁用相关推荐
                    if metadata.get('disable_related', False):
                        excluded_count += 1
                        continue
                    
                    # 再次检查是否在排除列表中（双重检查）
                    if is_page_excluded(file.src_path):
                        excluded_count += 1
                        continue
                    
                    # 提取关键词
                    keywords = extract_keywords(content, metadata['title'])
                    
                    # 获取分类
                    path_category = get_category_from_path(file.src_path)
                    
                    # 构建文章信息
                    article_info = {
                        'title': metadata['title'],
                        'description': metadata['description'],
                        'tags': metadata['tags'],
                        'categories': metadata['categories'],
                        'path_category': path_category,
                        'keywords': keywords,
                        'url': file.url,
                        'path': file.src_path,
                        'source_dir': file.src_path.split('/')[0]  # blog 或 develop
                    }
                    
                    # 添加到主索引
                    article_index[file.src_path] = article_info
                    
                    # 添加到分类索引
                    category_index[path_category].append(file.src_path)
                    for category in metadata['categories']:
                        if category:  # 确保分类不为空
                            category_index[category].append(file.src_path)
                    
                    # 添加到关键词索引
                    for keyword, _ in keywords:
                        keyword_index[keyword].add(file.src_path)
                    for tag in metadata['tags']:
                        if tag:  # 确保标签不为空
                            keyword_index[tag.lower()].add(file.src_path)
                    
                    processed_count += 1
                    
            except Exception as e:
                print(f"❌ 处理文件 {file.src_path} 时出错: {e}")
    
    # 第二遍：统计全局文档频率（IDF 用），每篇文章的关键词视为该文档的词集合
    total_docs = processed_count
    for info in article_index.values():
        # 一篇文档对一个词只计数一次（文档频率）
        for term, _ in info['keywords']:
            global_doc_freq[term] += 1
        for tag in info['tags']:
            if tag:
                global_doc_freq[tag.lower()] += 1
    
    print(f"✅ 已索引 {processed_count} 篇文章 (blog + develop)")
    if excluded_count > 0:
        print(f"📝 排除 {excluded_count} 篇禁用推荐或在排除列表中的文章")
    print(f"📊 分类数量: {len(category_index)}")
    print(f"🔤 关键词数量: {len(keyword_index)}")
    return files

def on_page_markdown(markdown, **kwargs):
    """为每篇文章添加相关推荐"""
    page = kwargs['page']
    config = kwargs['config']
    
    # 检查是否应该处理这个页面
    if not should_index_file(page.file.src_path):
        return markdown
    
    # 检查是否被排除
    if is_page_excluded(page.file.src_path):
        return markdown
    
    # 检查文章元数据是否禁用推荐
    try:
        with open(page.file.abs_src_path, 'r', encoding='utf-8') as f:
            content = f.read()
            metadata = extract_metadata(content)
            if metadata.get('disable_related', False):
                return markdown
    except Exception:
        pass  # 如果读取失败，继续处理
    
    # 获取相关文章
    related_articles = get_related_articles(page.file.src_path, max_count=5)
    
    if not related_articles:
        return markdown
    
    # 从 config 中获取 site_url 作为拼接基准
    site_url = config.get('site_url', '') or '/'

    # 构建推荐HTML - 针对Safari浏览器优化
    recommendation_html = "\n"
    
    # 添加CSS样式，特别针对Safari浏览器优化
    recommendation_html += """<style>
.related-posts {
  margin-top: 1.5rem;
  padding-top: 0.75rem;
  border-top: 1px solid rgba(0,0,0,0.1);
  max-height: none !important; /* 防止Safari错误计算高度 */
  overflow: visible !important; /* 防止内容被截断 */
}
.related-posts h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
  font-weight: 500;
  line-height: 1.3;
}
.related-posts ul {
  margin: 0 0 0.5rem 0 !important; /* 强制覆盖可能的冲突样式 */
  padding-left: 1.5rem;
  list-style-position: outside;
}
.related-posts li {
  margin-bottom: 0.25rem;
  line-height: 1.4;
}
/* 暗色模式适配 */
[data-md-color-scheme="slate"] .related-posts {
  border-top-color: rgba(255,255,255,0.1);
}
/* Safari特定修复 */
@supports (-webkit-hyphens:none) {
  .related-posts {
    display: block;
    position: relative;
    height: auto !important;
  }
  .related-posts ul {
    position: static;
  }
}
</style>
"""
    
    # 简化且兼容的HTML结构
    recommendation_html += '<div class="related-posts">\n'
    recommendation_html += '<h3>📚 相关文章推荐</h3>\n'
    recommendation_html += '<ul>\n'
    
    for score, article_info in related_articles:
        import html
        title = html.escape(article_info['title'])
        relative_url = article_info['url']
        full_url = urljoin(site_url, relative_url)
        recommendation_html += f'<li><a href="{full_url}">{title}</a></li>\n'
    
    recommendation_html += '</ul>\n'
    recommendation_html += '</div>\n'
    
    # 确保没有多余的空行
    return markdown.rstrip() + recommendation_html

def get_related_articles(current_path, max_count=5):
    """获取相关文章：归一化相似度排序 + MMR 多样性"""
    if current_path not in article_index:
        return []
    
    current_article = article_index[current_path]
    candidates = []
    
    for path, article_info in article_index.items():
        if path == current_path:
            continue
        if not article_info['title'].strip() or article_info['title'] == "未命名":
            continue
        if is_page_excluded(path):
            continue
        
        # 归一化后的综合相似度 [0,1]
        base = calculate_similarity(current_article, article_info)
        # 标题相似度作为加分项（同样已归一化）
        title_sim = calculate_title_similarity(current_article['title'], article_info['title'])
        score = base + title_sim * SIMILARITY_CONFIG['title_similarity']
        
        if score > SIMILARITY_CONFIG['min_threshold']:
            candidates.append((score, path, article_info))
    
    if not candidates:
        return []
    
    # 按综合相似度降序
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    # MMR：在「相关性」与「与已选集合的冗余度」之间权衡，逐条选取
    lam = SIMILARITY_CONFIG['mmr_lambda']
    selected = []
    selected_paths = set()
    remaining = candidates[:]  # 候选池（已按相关性排序）
    
    while len(selected) < max_count and remaining:
        best = None
        best_mmr = -1.0
        for idx, (score, path, info) in enumerate(remaining):
            if selected:
                # 与已选集合的最大相似度（冗余度）
                max_sim = max(calculate_similarity(s, info)
                              for _, s in selected)
            else:
                max_sim = 0.0
            mmr = lam * score - (1 - lam) * max_sim
            if mmr > best_mmr:
                best_mmr = mmr
                best = idx
        score, path, info = remaining.pop(best)
        selected.append((score, info))
        selected_paths.add(path)
    
    # 最终按相关性排序输出
    selected.sort(key=lambda x: x[0], reverse=True)
    return selected[:max_count]

def calculate_title_similarity(title1, title2):
    """计算两个标题的相似度（中英文混合，Jaccard）"""
    words1 = set(tokenize(title1))
    words2 = set(tokenize(title2))
    
    if not words1 or not words2:
        return 0
    
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    return intersection / union if union else 0

def _cosine(dict1, dict2):
    """两个带权向量（关键词 TF-IDF）的余弦相似度，归一到 [0,1]"""
    common = set(dict1) & set(dict2)
    if not common:
        return 0.0
    dot = sum(dict1[k] * dict2[k] for k in common)
    norm1 = math.sqrt(sum(v * v for v in dict1.values()))
    norm2 = math.sqrt(sum(v * v for v in dict2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot / (norm1 * norm2)

def _jaccard(set1, set2):
    """集合 Jaccard 相似度，归一到 [0,1]"""
    if not set1 or not set2:
        return 0.0
    inter = len(set1 & set2)
    union = len(set1 | set2)
    return inter / union if union else 0.0

def calculate_similarity(article1, article2):
    """计算两篇文章的综合相似度，各维度先归一化到 [0,1] 再加权"""
    weights = SIMILARITY_CONFIG['weights']
    score = 0.0
    
    # 1. 关键词相似度（TF-IDF 余弦，已归一化）
    kw1 = dict(article1['keywords'])
    kw2 = dict(article2['keywords'])
    if kw1 and kw2:
        score += _cosine(kw1, kw2) * weights['keywords']
    
    # 2. 标签相似度（Jaccard，已归一化）
    tags1 = {t.lower() for t in article1['tags'] if t}
    tags2 = {t.lower() for t in article2['tags'] if t}
    score += _jaccard(tags1, tags2) * weights['tags']
    
    # 3. 分类相似度（Jaccard，已归一化）
    cats1 = {c.lower() for c in article1['categories'] if c}
    cats2 = {c.lower() for c in article2['categories'] if c}
    score += _jaccard(cats1, cats2) * weights['categories']
    
    # 4. 路径分类相似度（0 或 1）
    if article1['path_category'] and article1['path_category'] == article2['path_category']:
        score += 1.0 * weights['path']
    
    # 5. 同源目录相似度（0 或 1）
    if article1.get('source_dir') and article1.get('source_dir') == article2.get('source_dir'):
        score += 1.0 * weights['source_dir']
    
    return score
