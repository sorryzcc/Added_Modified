import os
from datetime import datetime


def get_file_modification_times(directory):
    """
    获取指定目录及其子目录中所有文件的修改时间。

    参数:
        directory (str): 要扫描的目录路径。

    返回:
        list: 包含文件路径和修改时间的列表，每个元素是一个元组 (file_path, modification_time)。
    """
    file_times = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = os.path.getmtime(file_path)
            modification_time_formatted = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
            file_times.append((file_path, modification_time_formatted))
    return file_times


def main():
    directory = r'C:\Users\v_jinlqi\Desktop\scan_Added_Modified'  # 替换为你的目录路径
    file_times = get_file_modification_times(directory)

    # 打印所有文件的路径和修改时间
    for file_path, modification_time in file_times:
        print(f"文件路径: {file_path}, 修改时间: {modification_time}")


if __name__ == '__main__':
    main()
