# 🔧 修复URL问题指南

## 当前问题

网站可以通过以下URL访问：
- ✅ `https://easonai-5589.github.io/EasonAI.github.io/`

但无法通过根域名访问：
- ❌ `https://EasonAI-5589.github.io`

## 问题原因

这是因为GitHub Pages的部署设置问题。网站被部署到了子路径而不是根路径。

## 解决方案

### 方法1：检查GitHub Pages设置（推荐）

1. **访问GitHub Pages设置页面**：
   https://github.com/EasonAI-5589/EasonAI.github.io/settings/pages

2. **检查当前设置**：
   - Source: 应该设置为 "Deploy from a branch"
   - Branch: 应该选择 "main"
   - Folder: 应该选择 "/ (root)"

3. **如果设置不正确**：
   - 选择正确的设置
   - 点击 "Save"
   - 等待5-10分钟

### 方法2：检查仓库名称

确保仓库名称完全正确：
- 仓库名：`EasonAI.github.io`
- 用户名：`EasonAI-5589`

### 方法3：检查自定义域名设置

1. 在GitHub Pages设置页面
2. 检查是否有设置自定义域名
3. 如果有，请删除自定义域名设置

## 验证步骤

修复后，等待5-10分钟，然后测试：
- `https://EasonAI-5589.github.io`
- `https://easonai-5589.github.io`

## 如果问题持续

如果按照上述步骤操作后仍然无法通过根域名访问：

1. **等待更长时间**（最多1小时）
2. **检查Actions页面**确认构建成功
3. **联系GitHub支持**

## 临时解决方案

在问题解决之前，你可以：
1. 使用当前可访问的URL：`https://easonai-5589.github.io/EasonAI.github.io/`
2. 在社交媒体和简历中使用这个URL
3. 问题解决后更新为根域名

---

**最可能的情况是GitHub Pages设置中的Folder选项不正确，请检查设置页面。**
