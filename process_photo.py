#!/usr/bin/env python3
"""
处理个人照片，调整到合适的比例用于网站头像
"""

from PIL import Image
import os

def process_profile_photo(input_path, output_path, target_size=(400, 400)):
    """
    处理个人照片，调整到合适的比例
    
    Args:
        input_path: 输入照片路径
        output_path: 输出照片路径
        target_size: 目标尺寸 (width, height)
    """
    try:
        # 打开图片
        with Image.open(input_path) as img:
            print(f"原始图片尺寸: {img.size}")
            print(f"原始图片模式: {img.mode}")
            
            # 转换为RGB模式（如果是RGBA）
            if img.mode == 'RGBA':
                # 创建白色背景
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])  # 使用alpha通道作为mask
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 计算裁剪区域（保持正方形）
            width, height = img.size
            min_dim = min(width, height)
            
            # 计算裁剪的起始位置（居中裁剪）
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            
            # 裁剪为正方形
            img_cropped = img.crop((left, top, right, bottom))
            print(f"裁剪后尺寸: {img_cropped.size}")
            
            # 调整到目标尺寸
            img_resized = img_cropped.resize(target_size, Image.Resampling.LANCZOS)
            print(f"调整后尺寸: {img_resized.size}")
            
            # 保存图片
            img_resized.save(output_path, 'JPEG', quality=95, optimize=True)
            print(f"照片已保存到: {output_path}")
            
            # 获取文件大小
            file_size = os.path.getsize(output_path)
            print(f"文件大小: {file_size / 1024:.1f} KB")
            
    except Exception as e:
        print(f"处理照片时出错: {e}")

if __name__ == "__main__":
    # 处理照片
    input_photo = "/Users/guoyichen/EasonAI/academicpages-website/images/profile.png"
    output_photo = "/Users/guoyichen/EasonAI/academicpages-website/images/profile.jpg"
    
    print("开始处理个人照片...")
    process_profile_photo(input_photo, output_photo, target_size=(400, 400))
    print("照片处理完成！")
