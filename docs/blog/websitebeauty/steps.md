---
title: 用 Steps 容器展示步骤流程
tags:
  - Mkdocs
status: new
---

# 用 Steps 容器展示步骤流程

在写教程类文章时，经常会遇到「第一步、第二步、第三步」这种递进的操作指引。如果只用普通列表，可读性一般；而用 MaterialX 提供的 **Steps 容器**，可以把列表渲染成带圆形序号标记、有连接线的竖向步骤流，视觉上更有「引导感」。

参考文档：[MaterialX - Steps](https://jaywhj.github.io/mkdocs-materialx/reference/steps)

## 一个真实的例子

我的 Mkdocs 教程前言里，快速开始部分就用了这个写法（[`mkfirst.md`](https://github.com/Wcowin/Mkdocs-Wcowin/blob/main/docs/blog/Mkdocs/mkfirst.md)）：

```html
<div class="steps" markdown>

- [部署静态网页至GitHub pages](mkdocs1.md)
- [Mkdocs部署配置说明(mkdocs.yml)](mkdocs2.md)
- [网站添加Mkdocs博客](mkdocsblog.md)

</div>
```

<div class="steps" markdown>

- [部署静态网页至GitHub pages](../Mkdocs/mkdocs1.md)
- [Mkdocs部署配置说明(mkdocs.yml)](../Mkdocs/mkdocs2.md)
- [网站添加Mkdocs博客](../Mkdocs/mkdocsblog.md)

</div>

渲染出来就是三条带圆圈标记的「三部曲」引导链接，读者一眼就知道要按顺序看这三篇。

## 基础语法（列表模式）

Steps 本质上是一个带 `steps` 类的 `<div>`，加上 `markdown` 属性后，里面就可以正常写 Markdown 列表（有序、无序都支持）：

```html
<div class="steps" markdown>

1. Install
2. Configure
3. Run

</div>
```

也可以写成无序列表（也就是上面 mkfirst.md 的写法）：

```html
<div class="steps" markdown>

- First
- Second
- Third

</div>
```

`<div class="steps" markdown>` 和列表内容之间**必须留一个空行**，否则不会被正确解析。

## 使用前提

1. **MaterialX 版本 ≥ 10.2.0**（Steps 容器是 MaterialX 的增强特性）。
2. **开启 `md_in_html` 扩展**，让 HTML 标签内部能解析 Markdown。本仓库的 `mkdocs.yml` 已开启：

```yaml hl_lines="2"
markdown_extensions:
  - md_in_html
```

## 进阶：步骤里放复杂内容

Steps 列表项里不仅可以放文字和链接，还能嵌套提示框（admonition）、代码块等。例如：

```html
<div class="steps" markdown>

1. 安装依赖

    ```bash
    pip install mkdocs-materialx
    ```

2. 修改配置

    !!! tip "提示"
        记得开启 `md_in_html` 扩展。

3. 启动预览

</div>
```

## 自定义样式

步骤圆圈的颜色、连线、缩进等都可以通过 `extra.css` 里的 `--md-steps-*` 变量自定义。例如修改圆圈主题色：

```css
:root {
  --md-steps-color: #518FC1;
}
```

更多变量可参考 MaterialX 官方文档对应的 Steps 章节。

## 小结

- `Steps` 容器 = `<div class="steps" markdown>` + 列表，适合展示操作步骤。
- 需要 MaterialX ≥ 10.2.0 且开启 `md_in_html`。
- 比普通列表更直观，是教程类页面的好帮手。
