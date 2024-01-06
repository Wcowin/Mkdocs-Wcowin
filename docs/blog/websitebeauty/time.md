---
title: 为MKdocs添加文章修订时间戳
tags:
  - Mkdocs
comments: false  #评论，默认不开启
---

![img](https://cn.mcecy.com/image/20240106/ee0ece547112ac1b67fb61ac7f9c1a90.png)  

参考方法：[git 修订日期本地化](https://squidfunk.github.io/mkdocs-material/setup/adding-a-git-repository/#revisioning)

利用[git -revision-date-localized插件](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)添加了对添加上次更新日期和在每个页面底部创建文档的支持

## 安装

```bash
pip install mkdocs-git-revision-date-localized-plugin
```

## 配置

然后将以下行添加到mkdocs.yml：
```yml
plugins:
  - git-revision-date-localized:
      enable_creation_date: true
```

详细的配置请看：[mkdocs-git-revision-date-localized-plugin](https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/index.html)

可选的配置很多：
```yml
plugins:
  - git-revision-date-localized:
      type: timeago #时间类型
      custom_format: "%d. %B %Y"  # 时间格式
      timezone: Europe/Amsterdam #时区
      locale: en #首选语言
      fallback_to_build_date: false #许回退到git 不可用时mkdocs build执行的时间
      enable_creation_date: true #是否启用创建时间
      exclude:  #排除的页面
          - index.md
      enabled: true #是否启用
      strict: true
```

## 温馨提示

对于大型单一的文档库，执行`mkdocs serve`后的渲染速度明显变慢，这是因为每次渲染都会检查所有文件的git历史记录。如果您不需要这个功能，可以通过将`enabled`设置为`false`来禁用它。