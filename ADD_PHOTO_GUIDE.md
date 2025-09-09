# 📸 添加个人照片指南

## 步骤1：保存照片到images目录

请将你的照片保存到以下位置：

```bash
# 方法1：替换现有的profile.png（推荐）
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/profile.png

# 方法2：使用新文件名
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/yichen-photo.jpg
```

## 步骤2：更新配置文件

### 如果使用profile.png（推荐）
配置文件已经设置为使用`profile.png`，无需修改。

### 如果使用新文件名
需要修改`_config.yml`文件：

```yaml
author:
  avatar: "yichen-photo.jpg"  # 改为你的照片文件名
```

## 步骤3：照片要求

- **格式**：JPG、PNG都可以
- **尺寸**：建议400x400像素或更大
- **文件大小**：建议小于2MB
- **质量**：清晰、光线良好

## 步骤4：预览效果

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

然后访问 http://localhost:4000 查看效果

## 步骤5：提交更改

```bash
git add images/your-photo.jpg
git commit -m "Add personal photo"
git push origin main
```

## 照片显示位置

照片会在以下位置显示：
1. **侧边栏头像** - 在关于页面和个人资料页面
2. **作者信息** - 在博客文章和出版物页面
3. **社交媒体分享** - 当分享链接时显示

---

**提示**：你的照片背景是城市夜景，非常适合学术网站，既专业又有个性！
