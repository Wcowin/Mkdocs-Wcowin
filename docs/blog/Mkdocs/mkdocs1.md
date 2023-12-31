---
title: 利用Mkdocs部署静态网页至GitHubpages
tags:
  - Mkdocs
---

!!! info
    官方网站：[MkDocs](https://www.mkdocs.org/){target=“_blank”}

    我的个人网站成果：<http://wcowin.work/>{target=“_blank”}

## 一、准备工作(重要)

1.下载[Github Desktop](https://github.com/desktop/desktop){target=“_blank”}  

2.有一个GitHub账号​​​​​​​  

3.打开电脑终端安装mkdocs:  `pip install mkdocs-material`

***
## 二、Creating your site

参考教程： 

[利用mkdocs部署静态网页至GitHubpages（更新版）](https://blog.csdn.net/m0_63203517/article/details/129755527?spm=1001.2014.3001.5501){target=“_blank”}

与其他教程不同，我首先建议先在Github创建一个名为你的名字+github.io的仓库(不是这个名字的仓库也可以，你需要类比一下)
![img](https://cn.mcecy.com/image/20230324/51a12510e3b332b6ceea6827f40c1f2f.png)
![img](https://cn.mcecy.com/image/20230324/7f19bb393e39fb9add953ee19f9e2d91.png)  

然后打开github Desktop 克隆到本地
![img](https://cn.mcecy.com/image/20230324/ff3682428cc987cad79625951ef6d7bc.png)
![img](https://cn.mcecy.com/image/20230324/e896de95bd6fa737e7c6c3fa21c079fb.png)
![img](https://cn.mcecy.com/image/20230324/791834a5ac01c95ef174ab77d47c0f3a.png) 
![img](https://cn.mcecy.com/image/20230324/80430d0f8be7ea09368c3e63fe5a91ff.png)
打开Wcowin.github.io目录进入终端运行:
```
mkdocs new mkdocs-site
```
出现下图的几个文件 
![img](https://cn.mcecy.com/image/20230324/2f3f28cb5ee726ac154102de2ffb43da.png)

docs文件下是以后网站的内容，mkdocs.yml是配置文件（配置主题，目录，插件等）

 你在这个目录下写的任何东西都可以通过github Desktop 上传到github上

以VScode为例我们打开具体看看里面的东西

(必须先执行下面的代码添加一个GitHub Workflow)

``` 
mkdir .github
cd .github
mkdir workflows
cd workflows
vim PublishMySite.yml
```

在PublishMySite.yml里面输入以下内容

```
name: publish site
on: # 在什么时候触发工作流
  push: # 在从本地main分支被push到GitHub仓库时
    branches:
      - main
  pull_request: # 在main分支合并别人提的pr时
    branches:
      - main
jobs: # 工作流的具体内容
  deploy:
    runs-on: ubuntu-latest # 创建一个新的云端虚拟机 使用最新Ubuntu系统
    steps:
      - uses: actions/checkout@v2 # 先checkout到main分支
      - uses: actions/setup-python@v2 # 再安装Python3和相关环境
        with:
          python-version: 3.x
      - run: pip install mkdocs-material # 使用pip包管理工具安装mkdocs-material
      - run: mkdocs gh-deploy --force # 使用mkdocs-material部署gh-pages分支

```

!!!重点来了
仓库setings/Actions/General  勾选这两项
![](https://cn.mcecy.com/image/20231014/60f48ab66eea11b52f572b8fd489ea92.png)

目录树状图:
```
$ tree -a
.
├── .github
│   ├── .DS_Store
│   └── workflows
│       └── PublishMySite.yml
├── docs
│   └── index.md
└── mkdocs.yml
```
## 三、配置完善
打开终端运行  

`pip install mkdocs-material`

打开**mkdocs.yml** 

 把以下的内容输入进去（最简单配置）  

```
site_name: 网站名字
```

```
site_url: 网站链接
```

```
site_author: 你的名字
```

```
theme:
  name: material #主题
```  


详细mkdocs.yml配置见[Changing the colors - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/)

[下次](https://blog.csdn.net/m0_63203517/article/details/127444446?spm=1001.2014.3001.5502)我会具体谈谈这个问题
***
在下方终端运行可以在浏览器看到实时网站
```
mkdocs serve
```
![img](https://cn.mcecy.com/image/20230324/f11af9fb64a8418181bc3655a88d8635.png)
![img](https://cn.mcecy.com/image/20230324/c745b71840c17d639e1ea144bc8c5732.png)

这个网站就算是初步建好了

最后去github Desktop上传到github
![img](https://cn.mcecy.com/image/20230324/53ad3fdbe7d05668b99a46780930845a.png)

!!!重点来了
去setings/pages  选择下图示意的路径
![](https://cn.mcecy.com/image/20231014/ac6d1bc1a236737a18d9dd6bd2bd97dc.png)

你的网站网址就是：​

```
https://你github的名字.github.io/  （根据仓库名改变）
```
![img](https://cn.mcecy.com/image/20230324/51a12510e3b332b6ceea6827f40c1f2f.png)

## 快速开始
打开终端安装mkdocs: `pip install mkdocs-material`，在你第二步克隆到本地的文件夹下(比如我的就是Wcowin.github.io这个文件夹)的终端执行`git clone git@github.com:Wcowin/Mkdocs-Wcowin.git`克隆本模版,把Mkdocs-Wcowin文件里的文件复制出来到Wcowin.github.io文件里，随后在Wcowin.github.io文件目录终端里`mkdocs serve`即可

为了测试随手建的名为1的文件夹
![](https://cn.mcecy.com/image/20231014/f94d765bd86d56d35f7d558270d21bd5.png)  

完美运行！  

![](https://cn.mcecy.com/image/20231014/af910d370c91e06b8a6fc2e11ae3c6c9.png) 

**浏览器进入<http://127.0.0.1:8000/>{target=“_blank”}即可看到端口网页效果**

下次谈谈网站的[mkdocs.yml具体配置](mkdocs2.md)

[^注]:于2023.3.24重写此文