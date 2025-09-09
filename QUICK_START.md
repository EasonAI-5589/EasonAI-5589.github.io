# 🚀 快速开始指南

## 你的GitHub信息
- **用户名**: EasonAI-5589
- **网站地址**: https://EasonAI-5589.github.io

## 步骤1: 创建GitHub仓库

1. 访问 https://github.com
2. 点击右上角的 "+" 号 → "New repository"
3. 仓库名称：`EasonAI-5589.github.io`（必须完全匹配）
4. 描述：`EasonAI's Personal Academic Website`
5. 设置为 **Public** 仓库
6. **不要**勾选任何初始化选项
7. 点击 "Create repository"

## 步骤2: 推送代码到GitHub

在终端中运行：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
./setup_github.sh
```

或者手动运行：

```bash
git remote add origin https://github.com/EasonAI-5589/EasonAI-5589.github.io.git
git branch -M main
git push -u origin main
```

## 步骤3: 启用GitHub Pages

1. 访问 https://github.com/EasonAI-5589/EasonAI-5589.github.io
2. 点击 "Settings" 标签
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 下选择 "Deploy from a branch"
5. 选择 "main" 分支和 "/ (root)" 文件夹
6. 点击 "Save"

## 步骤4: 等待部署

- 等待5-10分钟让GitHub Pages部署完成
- 访问 https://EasonAI-5589.github.io 查看你的网站

## 本地开发

启动本地服务器：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

然后访问 http://localhost:4000

## 自定义网站

### 修改个人信息
- 编辑 `_config.yml` - 网站标题、描述等
- 编辑 `_pages/about.md` - 关于页面
- 替换 `images/bio-photo.jpg` - 个人照片
- 编辑 `_data/authors.yml` - 作者信息

### 添加内容
- 出版物：在 `_publications/` 目录添加 `.md` 文件
- 博客文章：在 `_posts/` 目录添加 `.md` 文件
- 项目：在 `_portfolio/` 目录添加 `.md` 文件
- 演讲：在 `_talks/` 目录添加 `.md` 文件

## 故障排除

如果遇到问题：
1. 确保Ruby版本正确：`ruby --version`
2. 重新安装依赖：`bundle install`
3. 检查Jekyll版本：`bundle exec jekyll --version`

---

🎉 **完成！** 你的个人学术网站现在可以被全世界访问了！
