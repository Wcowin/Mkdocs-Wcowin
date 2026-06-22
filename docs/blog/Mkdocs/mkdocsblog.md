---
title: 网站添加Mkdocs博客
tags:
  - Mkdocs
---  

博客效果展示：[博客](../index.md)  

官方文档：[Built-in blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/)

与所有内置插件一样，博客插件的入门非常简单。只需将以下行添加到mkdocs.yml

``` hl_lines="2"
plugins:
  - blog
```

**然后在/docs/blog/posts下写md文件即可**（无需再mkdocs.yml配置，如没有posts文件夹，新建一个即可）

!!! note "目录结构"
    插件会自动创建所需的目录结构。如果不存在，插件会创建：
    ```
    docs/
    └── blog/
        ├── posts/      # 博客文章存放目录
        └── index.md    # 博客首页（必需）
    ```

在mkdocs.yml的nav部分这样写：

!!! tip "重要提示"
    如果您的`mkdocs.yml`中已经定义了`nav`结构，需要启用`navigation.indexes`功能才能正确显示博客：

```yaml
theme:
  features:
    - navigation.indexes  # 必需，用于显示博客索引页
```

然后在nav部分添加博客：

```yaml
nav:
  - 博客:
      - index: blog/index.md
```

元标签参考（每个博客文章必须包含`date`字段）：

```yaml
---
title: 文章标题
authors: [Wcowin]  # 作者（对应.authors.yml中的标识符）
date: 2023-10-04   # 发布日期（必需）
draft: true        # 是否为草稿（可选）
categories:        # 分类（可选）
  - Hello
---
```  


作者信息在docs/blog/.authors.yml里配置（没有.authors.yml新建即可）  

```yml
authors:
  Wcowin:
    name: Wang Kewen    # Author name
    description: Free and casual # Author description
    avatar: https://s1.imagehub.cc/images/2024/02/02/91a767e93d1a344e44c69936464c583e.png          # Author avatar

```  

## 完整配置示例

```yaml
plugins:
  - blog:
      post_date_format: full        # 日期格式：full/long/medium/short
      draft: true                  # 构建时是否包含草稿
      draft_if_future_date: true   # 自动将未来日期的文章标记为草稿
      post_readtime: true          # 显示阅读时间
      post_readtime_words_per_minute: 265  # 每分钟阅读字数
      post_url_format: "{date}/{slug}"      # URL格式
```

更多配置选项请参考[官方文档](https://squidfunk.github.io/mkdocs-material/plugins/blog/)。
