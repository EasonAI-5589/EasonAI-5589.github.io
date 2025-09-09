# 📸 照片优化指南

## 你的照片特点

根据你提供的照片，这是一张非常棒的个人照片：
- **背景**：城市夜景，灯火辉煌的桥梁和摩天大楼
- **人物**：专业、友好的形象
- **构图**：右侧人物，左侧城市景观，平衡感很好
- **光线**：夜景灯光，营造专业氛围

## 照片要求

### 推荐规格
- **尺寸**：400x400像素（正方形）或 400x600像素（竖版）
- **格式**：JPG（文件小）或PNG（质量高）
- **文件大小**：建议小于2MB
- **质量**：清晰，光线良好

### 当前设置
网站已配置为使用 `profile.png` 作为头像

## 添加步骤

### 方法1：直接替换（推荐）
```bash
# 将你的照片保存为profile.png
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/profile.png
```

### 方法2：使用新文件名
```bash
# 保存为新文件名
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/yichen-photo.jpg
```

如果使用方法2，需要修改 `_config.yml`：
```yaml
author:
  avatar: "yichen-photo.jpg"  # 改为你的文件名
```

## 照片显示位置

你的照片将在以下位置显示：

1. **侧边栏头像** - 在关于页面和个人资料页面
2. **作者信息** - 在博客文章和出版物页面  
3. **社交媒体分享** - 当分享链接时显示
4. **搜索结果** - 在搜索引擎结果中显示

## 优化建议

### 裁剪建议
- 保持人物在画面右侧
- 可以适当裁剪左侧城市背景
- 确保人物面部清晰可见

### 文件优化
- 使用图片压缩工具减小文件大小
- 保持高质量的同时控制文件大小
- 考虑创建不同尺寸的版本

## 预览和测试

添加照片后，运行以下命令预览：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
bundle exec jekyll serve
```

访问 http://localhost:4000 查看效果

## 提交更改

```bash
git add images/your-photo.jpg
git commit -m "Add personal photo - city nightscape background"
git push origin main
```

---

**你的照片非常适合学术网站！城市夜景背景既专业又有个性，完美展现了现代研究者的形象。** 🌃✨
