---
title: 解决Github Pages部署mkdocs自定义域名失效的问题
tags:
  - Mkdocs
---

## 解决方法

在`/docs`目录下创建一个名为`CNAME`的文件（无后缀），然后在里面填入你的域名（每行一个域名）：

```
yourdomain.com
```

或者子域名：
```
blog.yourdomain.com
```

!!! tip "原因"
    因为每次在 GitHub 仓库的 Settings > Pages > Custom domain 中添加域名后，GitHub 会在`gh-pages`分支自动生成一个 CNAME 文件。但是因为项目我们没有 pull 到本地，所以每次 push 之后 CNAME 信息被覆盖了。

!!! note "重要提示"
    1. CNAME文件必须放在`docs/`目录下，这样在构建时会自动复制到站点根目录
    2. 确保在`mkdocs.yml`中设置了正确的`site_url`：
       ```yaml
       site_url: https://yourdomain.com/
       ```
    3. 如果使用自定义域名，还需要在域名DNS设置中添加CNAME记录指向GitHub Pages


