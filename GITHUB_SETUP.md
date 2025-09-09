# GitHub仓库设置指南

## 步骤1：在GitHub上创建仓库

1. **打开GitHub网站**：访问 https://github.com
2. **登录你的账户**
3. **创建新仓库**：
   - 点击右上角的 "+" 号
   - 选择 "New repository"
   - 仓库名称：`guoyichen.github.io`（必须完全匹配）
   - 描述：`Guoyichen's Personal Academic Website`
   - 设置为 **Public** 仓库
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**勾选 "Choose a license"
   - 点击 "Create repository"

## 步骤2：连接本地仓库到GitHub

创建仓库后，GitHub会显示设置说明。在终端中运行以下命令：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
git remote add origin https://github.com/guoyichen/guoyichen.github.io.git
git branch -M main
git push -u origin main
```

## 步骤3：启用GitHub Pages

1. 在GitHub仓库页面，点击 "Settings" 标签
2. 在左侧菜单中找到 "Pages"
3. 在 "Source" 下选择 "Deploy from a branch"
4. 选择 "main" 分支和 "/ (root)" 文件夹
5. 点击 "Save"

## 步骤4：等待部署

GitHub Pages 通常需要5-10分钟来构建和部署你的网站。

部署完成后，你的网站将在以下地址可用：
**https://guoyichen.github.io**

## 步骤5：验证网站

访问 https://guoyichen.github.io 确认网站正常运行。

---

**注意**：如果你还没有GitHub账户，请先注册一个账户。
