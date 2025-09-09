# 🔄 重命名仓库指南

## 问题分析

**当前情况**：
- 仓库名：`EasonAI.github.io`
- 用户名：`EasonAI-5589`
- 当前URL：`https://easonai-5589.github.io/EasonAI.github.io/`

**期望结果**：
- 仓库名：`EasonAI-5589.github.io`
- 用户名：`EasonAI-5589`
- 新URL：`https://EasonAI-5589.github.io`

## 重命名步骤

### 步骤1：访问仓库设置
1. 访问：https://github.com/EasonAI-5589/EasonAI.github.io/settings
2. 滚动到页面底部

### 步骤2：重命名仓库
1. 在"Repository name"部分
2. 将名称从 `EasonAI.github.io` 改为 `EasonAI-5589.github.io`
3. 点击"Rename"按钮

### 步骤3：更新本地仓库
重命名后，需要更新本地仓库的远程URL：

```bash
cd /Users/guoyichen/EasonAI/academicpages-website
git remote set-url origin https://github.com/EasonAI-5589/EasonAI-5589.github.io.git
```

### 步骤4：验证更改
```bash
git remote -v
```

应该显示：
```
origin  https://github.com/EasonAI-5589/EasonAI-5589.github.io.git (fetch)
origin  https://github.com/EasonAI-5589/EasonAI-5589.github.io.git (push)
```

### 步骤5：推送代码
```bash
git push origin main
```

## 预期结果

重命名完成后：
- ✅ 网站URL：`https://EasonAI-5589.github.io`
- ✅ 直接访问根域名
- ✅ 无需子路径

## 注意事项

1. **重命名后**：旧的URL将不再工作
2. **GitHub Pages**：会自动重新部署
3. **等待时间**：5-15分钟让新URL生效
4. **更新链接**：记得更新所有引用旧URL的地方

## 如果重命名失败

如果重命名遇到问题：
1. 检查是否有其他仓库使用相同名称
2. 确保有足够的权限
3. 联系GitHub支持

---

**重命名仓库是解决URL问题的最佳方案！**
