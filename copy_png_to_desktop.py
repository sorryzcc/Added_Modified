import os
import shutil
import pandas as pd

def copy_png_files(input_file, target_dir, max_count=1000):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 初始化计数器和文件夹编号
    file_count = 0
    folder_index = 0
    current_folder = os.path.join(target_dir, f'folder_{folder_index}')
    os.makedirs(current_folder, exist_ok=True)
    
    # 遍历所有路径
    for _, row in df.iterrows():
        source_path = row['Path']
        
        # 检查文件是否存在
        if os.path.exists(source_path):
            # 构建目标路径
            target_path = os.path.join(current_folder, os.path.basename(source_path))
            
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
    input_file = 'updated_processed_svn_log.xlsx'
    target_dir = os.path.expanduser('~/Desktop/PNG_Files')
    
    # 拷贝PNG文件
    copy_png_files(input_file, target_dir)
    
    print(f"PNG文件已成功拷贝到 {target_dir}")