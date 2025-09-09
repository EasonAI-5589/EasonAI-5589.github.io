# 📸 修复照片显示问题

## 当前状态

- ✅ 网站可以正常访问：https://easonai-5589.github.io
- ✅ 配置文件正确：avatar设置为"profile.png"
- ✅ 照片文件存在：images/profile.png
- ❌ 照片不显示：可能是格式或路径问题

## 可能的原因

1. **照片格式问题**：PNG格式可能有问题
2. **文件大小问题**：文件可能太大
3. **路径问题**：Jekyll可能无法正确解析路径
4. **缓存问题**：浏览器或GitHub Pages缓存

## 解决方案

### 方案1：使用JPG格式（推荐）

```bash
# 将你的照片保存为JPG格式
cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/profile.jpg
```

然后修改配置文件：
```yaml
author:
  avatar: "profile.jpg"  # 改为JPG格式
```

### 方案2：检查现有照片

```bash
# 检查现有照片文件
file images/profile.png
ls -la images/profile.png
```

### 方案3：使用bio-photo.jpg

```bash
# 使用现有的bio-photo.jpg
cp images/bio-photo.jpg images/profile.jpg
```

然后修改配置文件：
```yaml
author:
  avatar: "profile.jpg"
```

## 推荐步骤

1. **准备你的照片**：
   - 格式：JPG（推荐）或PNG
   - 尺寸：400x400像素或更大
   - 文件大小：小于2MB

2. **添加照片**：
   ```bash
   cp /path/to/your/photo.jpg /Users/guoyichen/EasonAI/academicpages-website/images/profile.jpg
   ```

3. **修改配置文件**：
   编辑 `_config.yml`：
   ```yaml
   author:
     avatar: "profile.jpg"
   ```

4. **提交更改**：
   ```bash
   git add images/profile.jpg _config.yml
   git commit -m "Add personal photo in JPG format"
   git push origin main
   ```

5. **等待部署**：
   - 等待5-10分钟让GitHub Pages重新部署
   - 清除浏览器缓存

## 验证步骤

1. **本地预览**：
   ```bash
   export PATH="$HOME/.rbenv/bin:$PATH"
   eval "$(rbenv init -)"
   bundle exec jekyll serve
   ```
   访问 http://localhost:4000 查看照片

2. **在线验证**：
   访问 https://easonai-5589.github.io 查看照片

## 如果问题持续

如果按照上述步骤操作后照片仍然不显示：

1. **检查文件路径**：确保照片在正确的目录
2. **检查文件权限**：确保文件可读
3. **尝试不同格式**：JPG、PNG、GIF
4. **检查文件大小**：确保文件不太大
5. **清除缓存**：浏览器和GitHub Pages缓存

---

**建议使用JPG格式，这通常是最兼容的格式。**
