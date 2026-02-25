# 最好的MkDocs教程

> 最详细、最便捷、最前沿的MkDocs中文教程，与官方版本同步更新。包含视频教程和文字教程，从入门到进阶一应俱全。

## 教程资源

- **[视频教程](https://space.bilibili.com/1407028951/lists/4566631?type=series)**（B站 | 手把手教学）
- **[文字教程(语雀)](https://www.yuque.com/wcowin/mkdocs-wcowin)**（推荐）
- **[文字教程(CSDN)](https://blog.csdn.net/m0_63203517/category_12472184.html?spm=1001.2014.3001.5482)**
- **[文字教程(知乎)](https://www.zhihu.com/column/c_1754218140098387968)**


## 目录
- [最好的MkDocs教程](#最好的mkdocs教程)
  - [教程资源](#教程资源)
  - [目录](#目录)
  - [展示](#展示)
  - [来自Claude-4-Sonnet的肯定](#来自claude-4-sonnet的肯定)
  - [快速开始](#快速开始)
    - [环境要求](#环境要求)
    - [方法一：直接下载使用（推荐新手）](#方法一直接下载使用推荐新手)
    - [方法二：Git克隆使用](#方法二git克隆使用)
    - [方法三：GitHub模板创建](#方法三github模板创建)
    - [常见问题解决](#常见问题解决)
      - [依赖安装问题](#依赖安装问题)
      - [Python版本问题](#python版本问题)
      - [端口占用问题](#端口占用问题)
      - [权限问题](#权限问题)
    - [自定义配置](#自定义配置)
    - [部署到线上](#部署到线上)
  - [视频教程](#视频教程)
- [Connect with me](#connect-with-me)
  - [案例成果](#案例成果)
  - [Star History](#star-history)
  - [贡献者](#贡献者)
  - [请作者喝杯咖啡](#请作者喝杯咖啡)
  - [License](#license)

## 展示  

<center>

**主页**
![](https://pic4.zhimg.com/80/v2-b74491257518429555b9f58a3bdc1293_1440w.webp)   

**文章页**
![](https://s1.imagehub.cc/images/2024/02/02/c15305494c69f311a721c0878b648b22.png)  

**博客页**
![](https://pic1.zhimg.com/80/v2-652abf2464779ebc6e5790ecaccaadde_1440w.webp) 

**关于**
<img width="1355" alt="image" src="https://github.com/Wcowin/Mkdocs-Wcowin/assets/99159173/bfc10737-260c-44c7-b036-8c7dba52be24">

**标签页**
![img](https://s1.imagehub.cc/images/2024/02/02/d20f0562838a8396724f18bfd09e19e8.png)  

**简洁的友链页面**
![](https://pic2.zhimg.com/80/v2-551c0a6e858705f842e2984fd44ce7f7_1440w.webp)

**页面底部**
<img width="1363" alt="image" src="https://github.com/Wcowin/Mkdocs-Wcowin/assets/99159173/ac4db87b-396a-4d0e-99b5-51a1b316db33">

**Lighthouse测试结果**
<img width="1363" alt="image" src="https://pic3.zhimg.com/80/v2-afef47cac915ad51071fdc2f6d990b30_1440w.webp">

<img width="1363" alt="image" src="https://s2.loli.net/2025/02/13/M7dgcDiGOI28PQs.png">

</center>

## 来自Claude-4-Sonnet的肯定

![image](https://s1.imagehub.cc/images/2025/07/12/509bbab32399e1b22942d259c1433d09.png)

## 快速开始

### 环境要求

在开始之前，请确保你的系统已安装：

- **Python 3.8+** （推荐3.9或更高版本）
- **pip** （Python包管理器）
- **Git** （用于版本控制）

### 方法一：直接下载使用（推荐新手）

这是最简单的方式，适合初学者快速体验：

1. **下载模板**
   - 访问 [Releases页面](https://github.com/Wcowin/Mkdocs-Wcowin/releases)
   - 下载最新版本的 `Wcowin-for-MkDocs.zip`
   - 解压到你想要的目录（注意把`Wcowin-for-MkDocs`文件夹里的所有文件单独移动到你的项目目录下）
   - 比如你在本地新建了一个`myblog`文件夹，那么就把`Wcowin-for-MkDocs`文件夹里的所有文件单独移动到`myblog`文件夹下


2. **安装依赖**
   ```bash
   # 建议在虚拟环境中安装
   pip install -r requirements.txt
   ```

3. **启动预览**
   ```bash
   # 进入解压后的目录
   cd myblog
   
   # 启动本地服务器
   mkdocs serve
   ```

4. **查看效果**
   - 打开浏览器访问 `http://127.0.0.1:8000`
   - 实时预览你的网站

出现报错自行谷歌即可，也可以给我发邮件，我会及时回复。

### 方法二：Git克隆使用

适合有Git基础的用户：

1. **克隆仓库**
   ```bash
   # 克隆到本地
   git clone https://github.com/Wcowin/Mkdocs-Wcowin.git
   
   # 进入项目目录
   cd Mkdocs-Wcowin
   ```

2. **安装依赖**
   ```bash
   # 安装所有必需的包
   pip install -r requirements.txt
   ```

3. **启动服务**
   ```bash
   # 启动开发服务器
   mkdocs serve
  
   ```

### 方法三：GitHub模板创建

最适合想要部署到GitHub Pages的用户：

1. **使用模板创建仓库**
   - 点击 [使用此模板](https://github.com/new?template_name=Mkdocs-Wcowin&template_owner=Wcowin)
   - 创建你自己的仓库（建议命名为 `你的用户名.github.io`）

2. **克隆到本地**
   ```bash
   git clone https://github.com/你的用户名/你的仓库名.git
   cd 你的仓库名
   ```

3. **配置和部署**
   ```bash
   # 安装依赖
   pip install -r requirements.txt
   
   # 本地预览
   mkdocs serve
   
   # 部署到GitHub Pages
   mkdocs gh-deploy
   ```

### 常见问题解决

#### 依赖安装问题

如果遇到插件缺失错误：

```bash
# 单独安装缺失的插件
pip install mkdocs-git-committers-plugin-2
pip install mkdocs-glightbox
pip install mkdocs-git-revision-date-localized-plugin

# 或者一次性安装所有依赖
pip install -r requirements.txt
```

#### Python版本问题

如果提示Python版本过低：

```bash
# 检查Python版本
python --version

# 如果版本低于3.8，请升级Python
# 或使用虚拟环境
python -m venv mkdocs-env
source mkdocs-env/bin/activate  # Linux/Mac
# 或
mkdocs-env\Scripts\activate     # Windows
```

#### 端口占用问题

如果8000端口被占用：

```bash
# 使用其他端口
mkdocs serve -a 127.0.0.1:8080
```

#### 权限问题

如果遇到权限错误：

```bash
# 使用用户级安装
pip install --user -r requirements.txt
```

### 自定义配置

1. **修改网站信息** - 编辑 `mkdocs.yml` 文件
2. **添加内容** - 在 `docs/` 目录下添加Markdown文件，更新 `mkdocs.yml` 中的导航配置
3. **个性化样式** - 修改 `docs/stylesheets/extra.css`

更多详细教程请访问：[完整文档](https://wcowin.work/Mkdocs-Wcowin/)

### 部署到线上

**GitHub Pages部署：**
```bash
mkdocs gh-deploy
```

**其他平台部署：**
```bash
# 构建静态文件
mkdocs build

# 将site/目录上传到你的服务器
```

---

**提示：** 首次使用MkDocs建议观看[视频教程](#视频教程)，手把手教学。

## 视频教程

[Mkdocs中文教程视频](https://space.bilibili.com/1407028951/lists/4566631?type=series)（B站 | 手把手教学）

# Connect with me

<center>

**Wechat**  
  <a href="https://pic3.zhimg.com/80/v2-5ef3dde831c9d0a41fe35fabb0cb8784_1440w.webp" target="_blank">
   <center>
    <img src="https://pic3.zhimg.com/80/v2-5ef3dde831c9d0a41fe35fabb0cb8784_1440w.webp" style="width: 450px; height: auto;">
    </center>  
  </a>  

**Telegram**

  <a href="https://t.me/wecowin" target="_blank" >
   <center>
    <img src="https://pica.zhimg.com/80/v2-d5876bc0c8c756ecbba8ff410ed29c14_1440w.webp" style="width: 450px; height: auto;">
    </center>  
  </a>

</center>

## 案例成果

[Lenny's Web](https://lennychen.top)  
[苍镜月's docs](https://pale-illusions.github.io/my-mkdocs/)  
[世界天光的笔记本](https://lastwish.icu/)  
[Wen-Chieh Lee的生活](https://wenchiehlee.github.io/mkdocs-life/)
[BruceJin's Notebook](https://brucejqs.github.io/MyNotebook/)  
[0X10CC的代码空间](https://tang-jiapeng.github.io/)  
[GENG Wei's Homepage](https://wgeng.site/index.html)

谢谢你们~

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Wcowin/Mkdocs-Wcowin&type=Date)](https://star-history.com/#Wcowin/Mkdocs-Wcowin&Date)

![Alt](https://repobeats.axiom.co/api/embed/b824e1bf28f31c9fa190eb5079cc1d035e562e0b.svg "Repobeats analytics image")

## 贡献者
<a href="https://github.com/Wcowin/Mkdocs-Wcowin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Wcowin/Mkdocs-Wcowin" />
</a>

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

## 请作者喝杯咖啡

https://www.gitfish.dev/repo/Wcowin/Mkdocs-Wcowin

  <a href="https://pic2.zhimg.com/80/v2-4384c32173a239a1609309aa1b1ee9f9_1440w.webp" target="_blank">
   <center>
    <img src="https://pic2.zhimg.com/80/v2-4384c32173a239a1609309aa1b1ee9f9_1440w.webp" style="width: 450px; height: auto;">
    </center>  
  </a> 

## License

**MIT License**

Copyright (c) 2022-2026 Wang Kewen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.