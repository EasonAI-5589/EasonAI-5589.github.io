#!/usr/bin/env python3
"""
改进版：处理easonguo.PNG照片，提高分辨率并确保人物居中
"""

from PIL import Image
import os

def process_easonguo_photo_improved(input_path, output_path, target_size=(600, 600)):
    """
    改进版处理easonguo.PNG照片
    
    Args:
        input_path: 输入照片路径
        output_path: 输出照片路径
        target_size: 目标尺寸 (width, height) - 提高分辨率
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
            
            # 分析图片，找到人物位置
            width, height = img.size
            print(f"图片宽高比: {width/height:.2f}")
            
            # 由于原图是横向的，人物在右侧，我们需要智能裁剪
            # 从右侧开始裁剪，确保人物在中心
            if width > height:
                # 横向图片，从右侧裁剪
                crop_width = height  # 裁剪为正方形
                left = width - crop_width  # 从右侧开始
                top = 0
                right = width
                bottom = height
            else:
                # 纵向图片，居中裁剪
                crop_height = width
                left = 0
                top = (height - crop_height) // 2
                right = width
                bottom = top + crop_height
            
            # 裁剪为正方形，确保人物在中心
            img_cropped = img.crop((left, top, right, bottom))
            print(f"裁剪区域: ({left}, {top}, {right}, {bottom})")
            print(f"裁剪后尺寸: {img_cropped.size}")
            
            # 调整到更高的目标尺寸
            img_resized = img_cropped.resize(target_size, Image.Resampling.LANCZOS)
            print(f"调整后尺寸: {img_resized.size}")
            
            # 保存图片，提高质量
            img_resized.save(output_path, 'JPEG', quality=95, optimize=True)
            print(f"照片已保存到: {output_path}")
            
            # 获取文件大小
            file_size = os.path.getsize(output_path)
            print(f"文件大小: {file_size / 1024:.1f} KB")
            
    except Exception as e:
        print(f"处理照片时出错: {e}")

if __name__ == "__main__":
    # 处理easonguo.PNG照片，提高分辨率
    input_photo = "/Users/guoyichen/EasonAI/academicpages-website/images/easonguo.PNG"
    output_photo = "/Users/guoyichen/EasonAI/academicpages-website/images/profile.jpg"
    
    print("开始改进版处理easonguo.PNG照片...")
    print("目标：提高分辨率，确保人物居中")
    process_easonguo_photo_improved(input_photo, output_photo, target_size=(600, 600))
    print("照片处理完成！")
