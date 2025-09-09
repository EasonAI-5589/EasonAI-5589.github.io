#!/bin/bash

echo "🔍 检查GitHub Pages配置状态"
echo ""

# 检查仓库信息
echo "📋 仓库信息："
echo "   仓库地址: https://github.com/EasonAI-5589/EasonAI.github.io"
echo "   期望网站地址: https://EasonAI-5589.github.io"
echo ""

# 检查最近的提交
echo "📝 最近的提交："
git log --oneline -3
echo ""

# 检查分支状态
echo "🌿 当前分支："
git branch
echo ""

# 检查远程状态
echo "📡 远程仓库状态："
git remote -v
echo ""

# 测试URL访问
echo "🌐 测试URL访问："
echo "测试 https://EasonAI-5589.github.io ..."
curl -s -o /dev/null -w "   状态码: %{http_code}\n" https://EasonAI-5589.github.io

echo "测试 https://easonai-5589.github.io ..."
curl -s -o /dev/null -w "   状态码: %{http_code}\n" https://easonai-5589.github.io

echo "测试 https://easonai-5589.github.io/EasonAI.github.io/ ..."
curl -s -o /dev/null -w "   状态码: %{http_code}\n" https://easonai-5589.github.io/EasonAI.github.io/
echo ""

echo "🔧 需要检查的GitHub设置："
echo ""
echo "1. 访问GitHub仓库设置页面："
echo "   https://github.com/EasonAI-5589/EasonAI.github.io/settings/pages"
echo ""
echo "2. 确认以下设置："
echo "   - Source: 'Deploy from a branch'"
echo "   - Branch: 'main' (不是master)"
echo "   - Folder: '/ (root)'"
echo ""
echo "3. 如果设置不正确，请："
echo "   - 选择正确的设置"
echo "   - 点击 'Save'"
echo "   - 等待5-10分钟"
echo ""
echo "4. 检查Actions页面："
echo "   https://github.com/EasonAI-5589/EasonAI.github.io/actions"
echo "   - 查看是否有 'pages build and deployment' 工作流"
echo "   - 确认状态为绿色（成功）"
echo ""
echo "5. 可能的问题："
echo "   - GitHub Pages未启用"
echo "   - 分支设置错误（应该是main，不是master）"
echo "   - 构建失败"
echo "   - 域名设置问题"
echo ""
echo "6. 如果所有设置都正确，请等待更长时间（最多1小时）"
echo ""
echo "📧 如果问题持续，可以："
echo "   - 联系GitHub支持"
echo "   - 在GitHub Community Forum寻求帮助"
