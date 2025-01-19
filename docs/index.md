---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: false
---

<!--
____    __    ____  ______   ______   ____    __    ____  __  .__   __. 
\   \  /  \  /   / /      | /  __  \  \   \  /  \  /   / |  | |  \ |  | 
 \   \/    \/   / |  ,----'|  |  |  |  \   \/    \/   /  |  | |   \|  | 
  \            /  |  |     |  |  |  |   \            /   |  | |  . `  | 
   \    /\    /   |  `----.|  `--'  |    \    /\    /    |  | |  |\   | 
    \__/  \__/     \______| \______/      \__/  \__/     |__| |__| \__| 

 ___       ___     ____     ____     ___       ___    _____      __      _  
(  (       )  )   / ___)   / __ \   (  (       )  )  (_   _)    /  \    / ) 
 \  \  _  /  /   / /      / /  \ \   \  \  _  /  /     | |     / /\ \  / /  
  \  \/ \/  /   ( (      ( ()  () )   \  \/ \/  /      | |     ) ) ) ) ) )  
   )   _   (    ( (      ( ()  () )    )   _   (       | |    ( ( ( ( ( (   
   \  ( )  /     \ \___   \ \__/ /     \  ( )  /      _| |__  / /  \ \/ /   
    \_/ \_/       \____)   \____/       \_/ \_/      /_____( (_/    \__/    
                                                                            
-->

<center><font  color= #518FC1 size=6 class="ml3">Mkdocs博客主题</font></center>
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>

<!-- <center>
<font  color= #608DBD size=3>
<span id="jinrishici-sentence">正在加载今日诗词....</span>
<script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
</font>
</center> -->


<!-- 可选一言 -->
<!-- <center>
<font  color= #608DBD size=3>
<p id="hitokoto">
  <a href="#" id="hitokoto_text" target="_blank"></a>
</p>
<script>
  fetch('https://v1.hitokoto.cn')
    .then(response => response.json())
    .then(data => {
      const hitokoto = document.querySelector('#hitokoto_text')
      hitokoto.href = `https://hitokoto.cn/?uuid=${data.uuid}`
      hitokoto.innerText = data.hitokoto
    })
    .catch(console.error)
</script>
</font>
</center> -->


<div id="rcorners2" >
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
</div> 






<!-- - 基于Material for MkDocs美化
- 简洁美观，功能多元化
- 简单易上手，小白配置
- 𝕙𝕒𝕧𝕖 𝕒 𝕘𝕠𝕠𝕕 𝕥𝕚𝕞𝕖 ! -->

视频教程(1) 联系我(2)
{ .annotate }

1. 点击右下角[:simple-bilibili:](https://space.bilibili.com/1407028951/lists/4566631?type=series)图标查看视频教程.
2. TEL:18939533255(微信号)

***  

<!-- <strong>推荐文章:material-book:</strong>

  - [利用Mkdocs部署静态网页至GitHub pages](blog/Mkdocs/mkdocs1.md)
  - [Mkdocs部署配置说明(mkdocs.yml)](blog/Mkdocs/mkdocs2.md)
  - [如何给MKdocs添加友链](blog/websitebeauty/linktech.md)
  - [网站添加Mkdocs博客](blog/Mkdocs/mkdocsblog.md)
  - [Blogger](blog/index.md) -->



<div class="grid cards" markdown>

-   :simple-materialformkdocs:{ .lg .middle } __Mkdocs教程__

    ---

    - [Mkdocs视频教程](https://space.bilibili.com/1407028951/lists/4566631?type=series){target=“_blank”}
    - [部署静态网页至GitHub pages](blog/Mkdocs/mkdocs1.md)
    - [Mkdocs部署配置说明(mkdocs.yml)](blog/Mkdocs/mkdocs2.md)
    - [如何给MKdocs添加友链](blog/websitebeauty/linktech.md)
    - [网站添加Mkdocs博客](blog/Mkdocs/mkdocsblog.md)



-   :simple-aboutdotme:{ .lg .middle } __关于__

    ---
    - [Mkdocs-Wcowin博客主题社区](https://support.qq.com/products/646913/){target=“_blank”}
    - [留言板](liuyanban.md)[^Knowing-that-loving-you-has-no-ending] 
    - [Blogger](blog/index.md)   
    [:octicons-arrow-right-24: 了解我](about/geren.md)[^see-how-much-I-love-you]

</div>



[^Knowing-that-loving-you-has-no-ending]:太阳总是能温暖向日葵  
[^see-how-much-I-love-you]:All-problems-in-computer-science-can-be-solved-by-another-level-of-indirection

   <body>
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
    </body>


<!-- <script src="//code.tidio.co/6jmawe9m5wy4ahvlhub2riyrnujz7xxi.js" async></script> -->


