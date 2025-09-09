#!/bin/bash

echo "🚀 设置GitHub仓库连接..."
echo ""

# 检查是否已经设置了远程仓库
if git remote get-url origin >/dev/null 2>&1; then
    echo "⚠️  远程仓库已经设置，正在移除..."
    git remote remove origin
fi

# 添加新的远程仓库
echo "📡 添加GitHub远程仓库..."
git remote add origin https://github.com/EasonAI-5589/EasonAI-5589.github.io.git

# 重命名分支为main
echo "🌿 重命名分支为main..."
git branch -M main

# 推送到GitHub
echo "⬆️  推送代码到GitHub..."
git push -u origin main

echo ""
echo "✅ 完成！"
echo ""
echo "🌐 你的网站将在以下地址可用："
echo "   https://EasonAI-5589.github.io"
echo ""
echo "📝 接下来请："
echo "   1. 访问 https://github.com/EasonAI-5589/EasonAI-5589.github.io"
echo "   2. 点击 Settings -> Pages"
echo "   3. 选择 'Deploy from a branch'"
echo "   4. 选择 'main' 分支和 '/ (root)' 文件夹"
echo "   5. 点击 Save"
echo ""
echo "⏰ 等待5-10分钟让GitHub Pages部署完成"
