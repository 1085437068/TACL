from PIL import Image
import os

def crop_images_to_512(input_folder, output_folder):
    # 如果输出目录不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # 确保是文件且是图片文件
        if os.path.isfile(file_path) and (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 获取图片的宽度和高度
                    width, height = img.size
                    
                    # 计算裁剪区域，保持原图比例居中裁剪
                    left = (width - 512) / 2
                    top = (height - 512) / 2
                    right = (width + 512) / 2
                    bottom = (height + 512) / 2
                    
                    # 裁剪图片
                    img_cropped = img.crop((left, top, right, bottom))
                    
                    # 构建输出文件路径
                    output_file_path = os.path.join(output_folder, filename)
                    
                    # 保存裁剪后的图片
                    img_cropped.save(output_file_path)
                    print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# 示例用法
input_folder = './trainB_origin'  # 输入文件夹路径
output_folder = './trainB'  # 输出文件夹路径
crop_images_to_512(input_folder, output_folder)