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
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.4s ease, visibility 0.4s ease;
            height: 0;
            overflow: hidden;
        }
        .comment-system.active {
            opacity: 1;
            visibility: visible;
            height: auto;
        }
        .button-container {
            text-align: center;
            margin: 20px 0;
        }
        .buttonxuan {
            background-color: white;
            width: 40%;
            color: black;
            border-radius: 18px;
            border: 2px solid rgba(189, 224, 245);
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition: 0.4s;
            cursor: pointer;
        }
        .buttonxuan:hover {
            background-color: rgba(238,242,249);
            color: rgb(4, 0, 0);
        }
        .buttonxuan.active {
            background-color: rgba(189, 224, 245);
            color: rgb(4, 0, 0);
        }
        @media (max-width: 768px) {
            .buttonxuan {
                padding: 10px 20px;
                font-size: 14px;
                margin: 5px;
                width: 100%;
                box-sizing: border-box;
            }
            .button-container {
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                flex-wrap: nowrap;
                gap: 5px;
            }
        }
    </style>
</head>
<body>
    <div class="button-container">
        <button id="giscus-btn" class="buttonxuan active">Giscus</button>
        <button id="cusdis-btn" class="buttonxuan">Cusdis</button>
    </div>
    <div id="giscus" class="comment-system active">
        <script src="https://giscus.app/client.js"
            data-repo="Wcowin/hexo-site-comments"
            data-repo-id="R_kgDOIl9OJA"
            data-category="Announcements"
            data-category-id="DIC_kwDOIl9OJM4CTHDe"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="top"
            data-theme="preferred_color_scheme"
            data-lang="zh-CN"
            data-loading="lazy"  
            crossorigin="anonymous"
            async>
        </script>
    </div>
    <div id="cusdis" class="comment-system">
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
        document.querySelectorAll('.buttonxuan').forEach(button => {
            button.addEventListener('click', function() {
                document.querySelectorAll('.buttonxuan').forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');
                document.querySelectorAll('.comment-system').forEach(system => system.classList.remove('active'));
                document.getElementById(this.id.replace('-btn', '')).classList.add('active');
            });
        });
    </script>
</body>