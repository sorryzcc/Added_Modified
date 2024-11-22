import os
import shutil

def copy_png_files(source_dir, target_dir, max_count=1000):
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 初始化计数器和文件夹编号
    file_count = 0
    folder_index = 0
    current_folder = os.path.join(target_dir, f'folder_{folder_index}')
    os.makedirs(current_folder, exist_ok=True)
    
    # 遍历源目录及其子目录中的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.png'):
                source_path = os.path.join(root, file)
                target_path = os.path.join(current_folder, file)
                
                # 检查源文件是否存在
                if os.path.exists(source_path):
                    # 拷贝文件
                    shutil.copy2(source_path, target_path)
                    print(f"Copied {source_path} to {target_path}")
                else:
                    print(f"Source file not found: {source_path}")
                
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
    source_dir = r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame\Assets\OuterResources\ABResources\UITextures\Mobile\DLC0\System\Activity_one'
    target_dir = os.path.expanduser('~/Desktop/PNG_Files')
    
    # 拷贝PNG文件
    copy_png_files(source_dir, target_dir)
    
    print(f"PNG文件已成功拷贝到 {target_dir}")