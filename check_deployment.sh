#!/bin/bash

echo "🔍 检查GitHub Pages部署状态"
echo ""

# 检查仓库信息
echo "📋 仓库信息："
echo "   仓库地址: https://github.com/EasonAI-5589/EasonAI.github.io"
echo "   网站地址: https://EasonAI-5589.github.io"
echo ""

# 检查最近的提交
echo "📝 最近的提交："
git log --oneline -3
echo ""

# 检查分支状态
echo "🌿 分支状态："
git branch -a
echo ""

# 检查远程状态
echo "📡 远程仓库状态："
git remote -v
echo ""

echo "🔧 请按照以下步骤检查GitHub Pages设置："
echo ""
echo "1. 访问GitHub仓库设置页面："
echo "   https://github.com/EasonAI-5589/EasonAI.github.io/settings/pages"
echo ""
echo "2. 检查以下设置："
echo "   - Source: 应该设置为 'Deploy from a branch'"
echo "   - Branch: 应该选择 'main' 分支"
echo "   - Folder: 应该选择 '/ (root)'"
echo ""
echo "3. 如果设置正确，等待5-10分钟让GitHub Pages部署"
echo ""
echo "4. 检查部署状态："
echo "   - 在仓库页面点击 'Actions' 标签"
echo "   - 查看是否有 'pages build and deployment' 工作流"
echo ""
echo "5. 如果仍然无法访问，可能的原因："
echo "   - GitHub Pages还在构建中（需要时间）"
echo "   - 网络问题或DNS解析问题"
echo "   - 浏览器缓存问题"
echo ""
echo "6. 尝试以下解决方案："
echo "   - 清除浏览器缓存"
echo "   - 使用无痕模式访问"
echo "   - 尝试不同的网络环境"
echo "   - 等待更长时间（有时需要15-30分钟）"
echo ""
echo "🌐 直接访问链接："
echo "   https://EasonAI-5589.github.io"
echo ""
echo "📧 如果问题持续，可以联系GitHub支持"
