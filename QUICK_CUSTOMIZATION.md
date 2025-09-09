# 🚀 快速自定义指南

## 第一步：修改基本信息

### 1. 编辑 `_config.yml` 文件

找到以下部分并修改：

```yaml
# 第12行附近
title: "EasonAI的个人网站"  # 改为你的网站标题

# 第14行附近  
name: "EasonAI"  # 改为你的姓名

# 第15行附近
description: "AI研究者和开发者"  # 改为你的描述

# 第16行附近
url: "https://EasonAI-5589.github.io"  # 改为你的网站地址

# 第23-32行附近 - 作者信息
author:
  avatar: "profile.png"  # 头像文件名
  name: "EasonAI"  # 你的姓名
  bio: "AI研究者和开发者，专注于机器学习和深度学习"  # 个人简介
  location: "中国"  # 你的位置
  employer: "你的公司/学校"  # 工作单位
  email: "your.email@example.com"  # 你的邮箱
```

### 2. 编辑 `_pages/about.md` 文件

将第3行的标题改为：
```markdown
title: "关于EasonAI"
```

将第10行开始的内容替换为你的个人介绍：
```markdown
# 关于我

我是EasonAI，一名AI研究者和开发者...

## 教育背景
- 学位，学校，年份

## 研究兴趣
- 机器学习
- 深度学习
- 自然语言处理

## 联系方式
- 邮箱：your.email@example.com
- GitHub：https://github.com/EasonAI-5589
```

## 第二步：添加个人照片

### 方法1：替换现有照片
```bash
# 将你的照片复制到images目录
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/profile.png
```

### 方法2：使用新文件名
1. 将照片上传到 `images/` 目录，命名为 `my-photo.jpg`
2. 在 `_config.yml` 中修改：
```yaml
author:
  avatar: "my-photo.jpg"  # 改为你的照片文件名
```

## 第三步：添加你的内容

### 添加一篇博客文章
在 `_posts/` 目录创建新文件，例如 `2024-09-09-welcome.md`：

```markdown
---
title: "欢迎来到我的网站"
date: 2024-09-09
permalink: /posts/2024/09/welcome/
tags:
  - 欢迎
  - 介绍
---

# 欢迎来到我的网站

这是我的第一篇博客文章...
```

### 添加一个项目
在 `_portfolio/` 目录创建新文件，例如 `my-project.md`：

```markdown
---
title: "我的AI项目"
excerpt: "一个基于深度学习的智能系统"
header:
  image: /images/project-image.jpg
---

# 我的AI项目

这是一个我开发的AI项目...
```

## 第四步：预览和发布

### 本地预览
```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

访问 http://localhost:4000 查看效果

### 发布到GitHub
```bash
git add .
git commit -m "自定义个人网站内容"
git push origin main
```

## 快速开始清单

- [ ] 修改 `_config.yml` 中的基本信息
- [ ] 编辑 `_pages/about.md` 中的个人介绍
- [ ] 上传个人照片到 `images/` 目录
- [ ] 添加一篇博客文章
- [ ] 添加一个项目展示
- [ ] 本地预览效果
- [ ] 推送到GitHub

---

🎉 **完成这些步骤后，你就有了一个个性化的个人网站！**
