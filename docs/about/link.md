---
title: 友链
comments: true
hide:
  #   - navigation # 显示右
  #   - toc #显示左
  - footer
  - feedback
---

<div class="markdown-content">
    <h2>欢迎加入友链(不分先后)</h2>
</div>

<div class="links-content">
  <div class="link-navigation">
    {% for friend in link.friends %}
    <div class="card">
      <img class="ava" src="{{ friend.avatar }}" />
      <div class="card-header">
        <div>
          <a href="{{ friend.link }}" target="_blank">{{ friend.name }}</a>
        </div>
        <div class="info">
          {{ friend.description }}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>


<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#608DBD,direction:145,strength:15)" width="100%" color=#608DBD SIZE=1>

<div class="markdown-content">
    <h2>失联人员</h2>
</div>
  <div class="links-content"> 
   <div class="link-navigation">

{% for gone in link.gone %}
    <div class="card"> 
     <img class="ava" src="{{gone.avatar}}" /> 
     <div class="card-header"> 
      <div> 
       <a href="{{gone.link}}" target="_blank">{{gone.name}}</a> 
      </div> 
      <div class="info">
       {{gone.description}}
      </div> 
     </div> 
    </div>
{% endfor %}

   </div> 
  </div>
<!-- <div class="card">
   <img class="ava" src="{avatarurl}" />
   <div class="card-header">
      <div>
         <a href="{link}">{name}</a>
      </div>
      <div class="info">{description}</div>
   </div>
</div> -->

<HR style="FILTER: progid:DXImageTransform.Microsoft.Shadow(color:#608DBD,direction:145,strength:15)" width="100%" color=#608DBD SIZE=1>

<div class="markdown-content">
    <h3>交换友链，请添加本站友链后下方留言申请，期望您的站点:</h3>
</div>

- 独立博客(不要求独立域名)，https，访问流畅
- 原创内容为主，原创内容 3 篇以上
- 处于活跃状态，有一定的更新频率
- 建站一个月以上
- 未添加友链或申请未通过，评论留言会被隐藏。

本站已经加入[十年之约](https://www.foreverblog.cn/)：
<a href="https://www.foreverblog.cn/" target="_blank" > <img src="https://img.foreverblog.cn/logo_en_default.png" alt="" style="width:auto;height:16px;"> </a>请放心添加本站友链

友链格式示例:

> 名称: Wcowin's Web  
> 链接: https://wcowin.work/  
> 头像: https://s2.loli.net/2024/02/01/gaE47y5fKM6kosV.png  
> 简介: 循此苦旅，以达星辰
