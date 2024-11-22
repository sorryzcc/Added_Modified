import os
import shutil

def copy_png_files(source_file, target_dir, max_count=1000):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 初始化计数器和文件夹编号
    file_count = 0
    folder_index = 0
    current_folder = os.path.join(target_dir, f'folder_{folder_index}')
    os.makedirs(current_folder, exist_ok=True)
    
    # 获取文件名
    file_name = os.path.basename(source_file)
    
    # 构建目标路径
    target_path = os.path.join(current_folder, file_name)
    
    # 检查源文件是否存在
    if os.path.exists(source_file):
        # 拷贝文件
        shutil.copy2(source_file, target_path)
        print(f"Copied {source_file} to {target_path}")
    else:
        print(f"Source file not found: {source_file}")
    
    # 更新计数器
    file_count += 1
    
    # 如果当前文件夹中的文件数量达到最大值，创建新的文件夹
    if file_count >= max_count:
        folder_index += 1
        current_folder = os.path.join(target_dir, f'folder_{folder_index}')
        os.makedirs(current_folder, exist_ok=True)
        file_count = 0

# 主函数
if __name__ == "__main__":
    source_file = r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame\CDNRes\Dev\B02\Default\Mall\Player\Bottom\t_Bottom_male_82.png'
    target_dir = os.path.expanduser('~/Desktop/PNG_Files')
    
    # 拷贝PNG文件
    copy_png_files(source_file, target_dir)
    
    print(f"PNG文件已成功拷贝到 {target_dir}")