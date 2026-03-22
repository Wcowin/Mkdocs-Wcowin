---
hide:
  # - navigation # 显示右
  # - toc #显示左
  - footer
  - feedback
comments: false
---

<!-- 公告栏 -->
<div class="oneclip-announcement">
  <div class="oneclip-announcement-content">
    🎉 <a href="https://wcowin.github.io/Zensical-Chinese-Tutorial/" target="_blank">Zensical中文教程</a> —— 最新zensical中文教程   <a href="https://wcowin.github.io/Zensical-Chinese-Tutorial/" target="_blank" class="oneclip-cta">了解更多 →</a>
    <br>
    ✨ 欢迎了解 <a href="https://github.com/jaywhj/mkdocs-materialx" target="_blank">mkdocs-materialx</a> —— 新版MkDocs主题   <a href="https://github.com/jaywhj/mkdocs-materialx" target="_blank" class="oneclip-cta">仓库地址｜</a> <a href="https://s1.imagehub.cc/images/2026/01/05/61035cc991bd4526ec304a223a2f0dc6.png" target="_blank">Wechat 群组</a>
  </div>
</div>
<!--
____    __    ____  ______   ______   ____    __    ____  __  .__   __. 
\   \  /  \  /   / /      | /  __  \  \   \  /  \  /   / |  | |  \ |  | 
 \   \/    \/   / |  ,----'|  |  |  |  \   \/    \/   /  |  | |   \|  | 
  \            /  |  |     |  |  |  |   \            /   |  | |  . `  | 
   \    /\    /   |  `----.|  `--'  |    \    /\    /    |  | |  |\   | 
    \__/  \__/     \______| \______/      \__/  \__/     |__| |__| \__| 
-->


<center><font class="custom-font ml3">最好的MkDocs中文教程</font></center>
<script src="https://cdn.statically.io/libs/animejs/2.0.2/anime.min.js"></script>
<style>
    .custom-font {
    font-size: 31px; /* 默认字体大小为8px */
    color: #757575;
}
@media (max-width: 768px) { /* 假设768px及以下为移动端 */
    .custom-font {
        font-size: 25px; /* 移动端字体大小为6px */
    }
}
</style>




<!-- <div id="rcorners2" >
<div id="rcorners1" class="date-display">
    <p class="p1"></p>
</div>
<style>
    .date-display {
        color: #4351AF;
    } 
</style>
<script defer>
    function format(newDate) {
        const options = {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            weekday: 'long',
            hour12: false
        };
        return new Intl.DateTimeFormat('zh-CN', options).format(newDate);
    }
    document.addEventListener('DOMContentLoaded', () => {
        const p1 = document.querySelector(".p1");
        function updateTime() {
            const newDate = new Date();
            if (p1) {
                p1.textContent = format(newDate);
            }
            requestAnimationFrame(updateTime);
        }
        updateTime();
    });
</script>
  <ul>
    <li>通过主题和目录以打开文章</li>
    <ul>
      <li>基于Material for MkDocs美化</li>
      <li>简洁美观，功能多元化，小白配置</li>
    </ul>
    <li>建议使用科学上网方式打开本站</li>
    <li>
      如遇到网页卡顿的情况，请使用<strong><a href="https://www.yuque.com/wcowin/mkdocs-wcowin?# 《Mkdocs-Wcowin中文教程》" target="_blank">Mkdocs-Wcowin中文教程(语雀)</a></strong>
    </li>
  </ul>
</div>  -->



<div class="grid cards" markdown>

-   :material-notebook-edit-outline:{ .lg .middle } __导航栏__

    ---
    ![image](https://pic3.zhimg.com/80/v2-0786a6086793ccca444226e9ab3561ec_1440w.webp){ class="responsive-image" align=right width="230" height="300" style="border-radius: 25px;" }

    
    - [x] {==简洁美观==} ，功能多元化，小白配置
    - [x] 基于{~~~>Material for MkDocs~~}美化
    - [x] 如遇页面卡顿，请使用{--科学上网--}
    - [x] 𝕙𝕒𝕧𝕖 𝕒 𝕘𝕠𝕠𝕕 𝕥𝕚𝕞𝕖 !  
    === "Mac/PC端"

        请在上方标签选择分类/左侧目录选择文章

    === "移动端"

        请点击左上角图标选择分类和文章
    

</div>
<style>
    @media only screen and (max-width: 768px) {
        .responsive-image {
            display: none;
        }
    }
</style>


>不同于市面上过时的MkDocs教程，本站提供了最详细最便捷最前沿的MkDocs中文文字/视频教程，与[官方发布](https://squidfunk.github.io/mkdocs-material/changelog/)的教程版本同步。包含了MkDocs的安装、配置、主题美化、插件使用等内容。无论你是初学者还是有经验的用户，都能在这里找到你需要的帮助。我们还提供了示例和实用的技巧，帮助你更好地使用MkDocs。𝓳𝓾𝓼𝓽 𝓮𝓷𝓳𝓸𝔂 𝓲𝓽～


!!! note "重要提醒"
    Mkdocs for material已经进入维护状态，[materialX](https://github.com/jaywhj/mkdocs-materialx)作为mkdocs的延续被广泛使用，本站作为mkdocs教程站迁移至materialX主题。
    [Zensical](https://github.com/zensical/zensical)是 mkdocs for material原作者的延续，提供了更丰富的功能和更现代的UI设计，可以考虑迁移至Zensical主题，我不再更新mkdocs for material教程。
    ---
    2026.3  目前 <https://github.com/ProperDocs> 作为新的mkdocs延续下去了，我只能说mkdocs圈真乱,本UP主已经全面拥抱Zensical了。吃瓜请去[这里](https://github.com/mkdocs/mkdocs/discussions/4077)。所以如果使用mkdocs，我首先还是推荐[materialX](https://github.com/jaywhj/mkdocs-materialx)

<!-- - 基于Material for MkDocs美化
- 简洁美观，功能多元化
- 简单易上手，小白配置
- 𝕙𝕒𝕧𝕖 𝕒 𝕘𝕠𝕠𝕕 𝕥𝕚𝕞𝕖 ! -->

<!-- 视频教程(1) 联系我(2)
{ .annotate }

1. 点击右下角[:simple-bilibili:](https://space.bilibili.com/1407028951/lists/4566631?type=series)图标查看视频教程.
2. TEL:18939533255(微信号) -->

***  

<!-- <strong>推荐文章:material-book:</strong>

  - [利用Mkdocs部署静态网页至GitHub pages](blog/Mkdocs/mkdocs1.md)
  - [Mkdocs部署配置说明(mkdocs.yml)](blog/Mkdocs/mkdocs2.md)
  - [如何给MKdocs添加友链](blog/websitebeauty/linktech.md)
  - [网站添加Mkdocs博客](blog/Mkdocs/mkdocsblog.md)
  - [Blogger](blog/index.md) -->



<div class="grid cards" markdown>

-   :simple-materialformkdocs:{ .lg .middle } __Mkdocs教程(必看)__

    ---

    - [Mkdocs视频教程](https://space.bilibili.com/1407028951/lists/4566631?type=series){target=“_blank”}(Bilibili)
    - [部署静态网页至GitHub pages](blog/Mkdocs/mkdocs1.md)
    - [Mkdocs部署配置说明(mkdocs.yml)](blog/Mkdocs/mkdocs2.md)
    - [如何给MKdocs添加友链](blog/websitebeauty/linktech.md)
    - [网站添加Mkdocs博客](blog/Mkdocs/mkdocsblog.md)



-   :simple-aboutdotme:{ .lg .middle } __关于__

    ---
    - [微信交流群](https://s1.imagehub.cc/images/2026/01/05/61035cc991bd4526ec304a223a2f0dc6.png){target=“_blank”}
    - [留言板](liuyanban.md)[^Knowing-that-loving-you-has-no-ending] 
    - [Blogger](blog/index.md)   
    - [:octicons-arrow-right-24: 了解我](about/geren.md)[^see-how-much-I-love-you]  
    - [请作者喝杯咖啡](about/zcw.md)

</div>

<!-- RECENTLY_UPDATED_DOCS -->

[^Knowing-that-loving-you-has-no-ending]:太阳总是能温暖向日葵  
[^see-how-much-I-love-you]:All-problems-in-computer-science-can-be-solved-by-another-level-of-indirection

   <!-- <body>
        <font color="#B9B9B9">
        <p style="text-align: center; ">
                <span>本站已经运行</span>
                <span id='box1'></span>
    </p>
      <div id="box1"></div>
      <script>
        function timingTime(){
          let start = '2023-10-14 00:00:00'
          let startTime = new Date(start).getTime()
          let currentTime = new Date().getTime()
          let difference = currentTime - startTime
          let m =  Math.floor(difference / (1000))
          let mm = m % 60  // 秒
          let f = Math.floor(m / 60)
          let ff = f % 60 // 分钟
          let s = Math.floor(f/ 60) // 小时
          let ss = s % 24
          let day = Math.floor(s  / 24 ) // 天数
          return day + "天" + ss + "时" + ff + "分" + mm +'秒'
        }
        setInterval(()=>{
          document.getElementById('box1').innerHTML = timingTime()
        },1000)
      </script>
      </font>
    </body> -->


<!-- <script src="//code.tidio.co/6jmawe9m5wy4ahvlhub2riyrnujz7xxi.js" async></script> -->



<!-- <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2327435979273742"
     crossorigin="anonymous"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2327435979273742"
     data-ad-slot="3702206121"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script> -->
<head> 
  <!-- Umami Analytics -->
  <script defer src="https://cloud.umami.is/script.js" data-website-id="061b4dea-9b7b-4ffa-9071-74cde70f3dfb"></script>
</head>
