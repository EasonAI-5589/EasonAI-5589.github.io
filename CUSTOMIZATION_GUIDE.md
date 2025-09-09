# 🎨 个人网站自定义指南

## 📸 1. 添加个人照片

### 方法1：替换现有照片
```bash
# 将你的照片复制到images目录，替换现有照片
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/bio-photo.jpg
```

### 方法2：使用新文件名
1. 将照片上传到 `images/` 目录
2. 编辑 `_data/authors.yml` 文件，修改照片路径

## 📝 2. 修改基本信息

### 编辑网站配置
编辑 `_config.yml` 文件：

```yaml
# 网站基本信息
title: "你的姓名"                    # 网站标题
tagline: "你的专业领域"              # 副标题
description: "你的个人描述"          # 网站描述
url: "https://EasonAI-5589.github.io"  # 你的网站地址
baseurl: ""                        # 基础URL

# 作者信息
author:
  name: "你的姓名"
  avatar: "/images/bio-photo.jpg"   # 头像路径
  bio: "你的个人简介"
  location: "你的位置"
  email: "your.email@example.com"
  links:
    - label: "Email"
      icon: "fas fa-envelope"
      url: "mailto:your.email@example.com"
    - label: "GitHub"
      icon: "fab fa-github"
      url: "https://github.com/EasonAI-5589"
    - label: "LinkedIn"
      icon: "fab fa-linkedin"
      url: "https://linkedin.com/in/yourprofile"
```

### 编辑关于页面
编辑 `_pages/about.md` 文件：

```markdown
---
title: "About"
permalink: /about/
layout: single
author_profile: true
---

# 关于我

这里写你的个人介绍...

## 教育背景
- 学位，学校，年份

## 研究兴趣
- 研究领域1
- 研究领域2

## 联系方式
- 邮箱：your.email@example.com
- 电话：+86 xxx-xxxx-xxxx
```

## 📚 3. 添加出版物

在 `_publications/` 目录下创建新的 `.md` 文件：

```markdown
---
title: "论文标题"
authors: "你的姓名, 合作者姓名"
venue: "期刊/会议名称"
year: 2024
type: "journal"  # 或 "conference"
pdf: "/files/paper.pdf"  # 可选：PDF文件路径
code: "https://github.com/your-repo"  # 可选：代码链接
demo: "https://your-demo.com"  # 可选：演示链接
---

论文摘要或描述...
```

## 📝 4. 添加博客文章

在 `_posts/` 目录下创建新的 `.md` 文件：

```markdown
---
title: "文章标题"
date: 2024-09-09
permalink: /posts/2024/09/文章标题/
tags:
  - 标签1
  - 标签2
---

# 文章标题

文章内容...
```

## 🎯 5. 添加项目

在 `_portfolio/` 目录下创建新的 `.md` 文件：

```markdown
---
title: "项目名称"
excerpt: "项目简短描述"
header:
  image: /images/project-image.jpg
  teaser: /images/project-teaser.jpg
---

# 项目名称

项目详细描述...

## 技术栈
- 技术1
- 技术2

## 链接
- [GitHub](https://github.com/your-repo)
- [演示](https://your-demo.com)
```

## 🎤 6. 添加演讲

在 `_talks/` 目录下创建新的 `.md` 文件：

```markdown
---
title: "演讲标题"
venue: "会议/活动名称"
date: 2024-09-09
location: "地点"
slides: "/files/slides.pdf"  # 可选：幻灯片
video: "https://youtube.com/watch?v=xxx"  # 可选：视频
---

演讲描述...
```

## 🎓 7. 添加教学经历

在 `_teaching/` 目录下创建新的 `.md` 文件：

```markdown
---
title: "课程名称"
venue: "学校名称"
date: 2024-09-09
location: "地点"
---

课程描述...
```

## 🔧 8. 本地预览更改

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

然后访问 http://localhost:4000 查看更改

## 📤 9. 推送更改到GitHub

```bash
git add .
git commit -m "更新个人网站内容"
git push origin main
```

## 💡 小贴士

1. **照片建议**：
   - 个人照片：400x400像素或更大
   - 项目图片：1200x600像素
   - 使用JPG或PNG格式

2. **文件命名**：
   - 使用英文和连字符
   - 避免空格和特殊字符

3. **内容更新**：
   - 每次修改后都要提交到Git
   - GitHub Pages会自动重新部署

4. **SEO优化**：
   - 在`_config.yml`中填写完整的描述
   - 为每篇文章添加合适的标签

---

🎉 **开始自定义你的个人网站吧！**
