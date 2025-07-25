---
title: 留言板
hide:
#   - navigation # 显示右
#   - toc #显示左
  - footer
  - feedback
comments: false
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Wcowin/Wcowin.github.io@main/docs/stylesheets/poem.css">


# 畅所欲言  
<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
  <h1>留言板</h1>
  <p id="poem">月落乌啼霜满天 江枫渔火对愁眠</p>
  <p id="info"> 《枫桥夜泊》&nbsp【唐代】&nbsp张继</p>
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
            transition: all 0.5s ease-in-out;
            height: 0;
            overflow: hidden;
            margin-top: 20px;
        }
        .comment-system.active {
            opacity: 1;
            visibility: visible;
            height: auto;
        }
        .button-container {
            text-align: center;
            margin: 30px auto;
            max-width: 600px;
        }
        .buttonxuan {
            background-color: #ffffff;
            width: 180px;
            color: #999;
            border-radius: 25px;
            border: 2px solid #1F2635;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 15px;
            font-weight: 500;
            margin: 0 10px;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .buttonxuan:hover {
            background-color: #f8f9fa;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        .buttonxuan.active {
            background-color: #1F2635;
            color: white;
            border-color: #1F2635;
        }
        @media (max-width: 768px) {
            .button-container {
                padding: 0 15px;
            }
            .buttonxuan {
                width: 45%;
                padding: 10px 15px;
                font-size: 14px;
                margin: 5px;
            }
        }
        @media (max-width: 480px) {
            .buttonxuan {
                width: calc(50% - 20px);
                font-size: 13px;
                padding: 8px 12px;
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