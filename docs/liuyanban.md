---
title: 留言板
hide:
#   - navigation # 显示右
#   - toc #显示左
  - footer
  - feedback
comments: false
---
# 畅所欲言  
<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
    <h1>留言板</h1>
    <p id="poem">月落乌啼霜满天 江枫渔火对愁眠</p>
    <p id="info"> 《枫桥夜泊》【唐代】张继</p>
  </div>


<!-- <div id="rcorners5" >
<div id="cusdis_thread"
  data-host="https://cusdis.com"
  data-app-id="655cf3bc-734a-4d88-8317-be350621334c"
  data-page-id="{{ PAGE_ID }}"
  data-page-url="{{ PAGE_URL }}"
  data-page-title="{{ PAGE_TITLE }}"
></div>
<script async defer src="https://cusdis.com/js/cusdis.es.js"></script>
<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>
</div> -->

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>评论系统切换</title>
    <style>
        .comment-system {
            display: none;
        }
        .comment-system.active {
            display: block;
        }
        .button-container {
            text-align: center;
            margin: 20px 0;
        }
        .switch-button {
            background-color: #608DBD;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .switch-button:hover {
            background-color: #4a6e8c;
        }
        .switch-button.active {
            background-color: #4a6e8c;
        }
    </style>
</head>
<body>
    <div class="button-container">
      <!-- <center><p>点击以切换评论系统</p></center> -->
        <button id="giscus-btn" class="switch-button active">Giscus 评论</button>
        <button id="cusdis-btn" class="switch-button">Cusdis 评论</button>
    </div>
    <div id="giscus" class="comment-system active">
        <!-- Giscus 评论系统代码 -->
  <script src="https://giscus.app/client.js"
  data-repo="Wcowin/hexo-site-comments"
  data-repo-id="R_kgDOIl9OJA"
  data-category="Announcements"
  data-category-id="DIC_kwDOIl9OJM4CTHDe"
  data-mapping="url"
  data-strict="0"
  data-reactions-enabled="1"
  data-emit-metadata="1"
  data-input-position="bottom"
  data-theme="preferred_color_scheme"
  data-lang="zh-CN"
  data-loading="lazy"  
  crossorigin="anonymous"
  async>
</script>
    </div>
    <div id="cusdis" class="comment-system">
        <!-- Cusdis 评论系统代码 -->
        <center><p>评论审核后才会显示</p></center>
        <div id="cusdis_thread"
            data-host="https://cusdis.com"
            data-app-id="655cf3bc-734a-4d88-8317-be350621334c"
            data-page-id="{{ PAGE_ID }}"
            data-page-url="{{ PAGE_URL }}"
            data-page-title="{{ PAGE_TITLE }}">
        </div>
        <script async defer src="https://cusdis.com/js/cusdis.es.js"></script>
    </div>
    <script>
        document.getElementById('giscus-btn').addEventListener('click', function() {
            document.getElementById('giscus').classList.add('active');
            document.getElementById('cusdis').classList.remove('active');
            this.classList.add('active');
            document.getElementById('cusdis-btn').classList.remove('active');
        });
        document.getElementById('cusdis-btn').addEventListener('click', function() {
            document.getElementById('giscus').classList.remove('active');
            document.getElementById('cusdis').classList.add('active');
            this.classList.add('active');
            document.getElementById('giscus-btn').classList.remove('active');
        });
    </script>
</body>