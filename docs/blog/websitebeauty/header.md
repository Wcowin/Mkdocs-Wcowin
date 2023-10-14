---
title: 添加顶部公告栏
# 隐藏的模块
hide:
  #  - navigation # 隐藏左边导航
  #  - toc #隐藏右边导航
  #  - footer #隐藏翻页
  #  - feedback  #隐藏反馈
tags:
  - Mkdocs
comments: false  #评论，默认不开启
---
![](https://cn.mcecy.com/image/20231014/28f7a934aed2790c02785638c06580c8.png)

overrides下新建main.html ，针对main.html文件  

树状结构如下
![](https://cn.mcecy.com/image/20231013/c9e5930308a1e0369c43499cf8f73e27.png)


```html
{#-
    This file was automatically generated - do not edit
  -#}
  {% extends "base.html" %}
  {% block extrahead %}
    <link rel="stylesheet" href="{{ 'assets/stylesheets/custom.00c04c01.min.css' | url }}">
  {% endblock %}
  {% block announce %}
     Follow <strong>@Wcowin</strong> on
    <a rel="me" href="https://space.bilibili.com/1407028951?spm_id_from=333.1007.0.0">
      <span class="twemoji bilibili">
        {% include ".icons/fontawesome/brands/bilibili.svg" %}
      </span>
      <strong>Bilibili</strong>
    </a>
    and
    <a href="https://twitter.com/Wcowin_">
      <span class="twemoji twitter">
        {% include ".icons/fontawesome/brands/twitter.svg" %}
      </span>
      <strong>Twitter</strong>
    </a>
  {% endblock %}
  {% block scripts %}
    {{ super() }}
    <script src="{{ 'assets/javascripts/custom.9458f965.min.js' | url }}"></script>
  {% endblock %}
```


自行修改即可
