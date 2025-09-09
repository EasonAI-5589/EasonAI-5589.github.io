# 个人网站设置说明

## 已完成的工作

✅ 已成功克隆 academicpages 仓库到本地
✅ 已安装所有必要的依赖（Ruby 3.1.0, Bundler, Node.js）
✅ 已安装项目依赖包
✅ 已测试本地服务器运行正常（http://localhost:4000）

## 下一步：设置你的GitHub仓库

### 1. 在GitHub上创建新仓库

1. 登录你的GitHub账户
2. 点击右上角的 "+" 号，选择 "New repository"
3. 仓库名称设置为：`你的用户名.github.io`（例如：`guoyichen.github.io`）
4. 设置为 Public 仓库
5. 不要初始化 README、.gitignore 或 license（因为我们已经有了）
6. 点击 "Create repository"

### 2. 连接本地仓库到GitHub

在终端中运行以下命令（将 `你的用户名` 替换为你的实际GitHub用户名）：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
git remote add origin https://github.com/你的用户名/你的用户名.github.io.git
git branch -M main
git push -u origin main
```

### 3. 启用GitHub Pages

1. 在GitHub仓库页面，点击 "Settings" 标签
2. 在左侧菜单中找到 "Pages"
3. 在 "Source" 下选择 "Deploy from a branch"
4. 选择 "main" 分支和 "/ (root)" 文件夹
5. 点击 "Save"

### 4. 等待部署

GitHub Pages 通常需要几分钟来构建和部署你的网站。部署完成后，你的网站将在以下地址可用：
`https://你的用户名.github.io`

## 自定义你的网站

### 修改个人信息

1. **编辑 `_config.yml`** - 修改网站标题、描述、作者信息等
2. **编辑 `_pages/about.md`** - 修改关于页面内容
3. **替换 `images/bio-photo.jpg`** - 上传你的个人照片
4. **编辑 `_data/authors.yml`** - 修改作者信息

### 添加内容

1. **添加出版物** - 在 `_publications/` 目录下添加新的 `.md` 文件
2. **添加博客文章** - 在 `_posts/` 目录下添加新的 `.md` 文件
3. **添加项目** - 在 `_portfolio/` 目录下添加新的 `.md` 文件
4. **添加演讲** - 在 `_talks/` 目录下添加新的 `.md` 文件

### 本地开发

要启动本地开发服务器：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

然后在浏览器中访问 `http://localhost:4000` 查看你的网站。

## 故障排除

如果遇到问题：

1. 确保Ruby版本正确：`ruby --version` 应该显示 3.1.0
2. 确保Bundler已安装：`bundle --version`
3. 重新安装依赖：`bundle install`
4. 检查Jekyll版本：`bundle exec jekyll --version`

## 有用的资源

- [AcademicPages 官方文档](https://academicpages.github.io/)
- [Jekyll 官方文档](https://jekyllrb.com/docs/)
- [GitHub Pages 文档](https://docs.github.com/en/pages)
