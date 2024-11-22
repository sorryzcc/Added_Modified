import pandas as pd

def filter_paths(input_file, output_file, exclude_prefixes):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 打印原始数据的前几行
    print("原始数据的前几行:")
    print(df.head())
    
    # 创建一个布尔掩码来过滤掉指定前缀的行
    mask = ~df['Path'].str.startswith(tuple(exclude_prefixes), na=False)
    
    # 应用掩码
    df_filtered = df[mask]
    
    # 打印过滤后的数据的前几行
    print("过滤后的数据的前几行:")
    print(df_filtered.head())
    
    # 保存为新的Excel文件
    df_filtered.to_excel(output_file, index=False)

# 主函数
if __name__ == "__main__":
    input_file = 'updated_processed_svn_log.xlsx'
    output_file = 'filtered_svn_log.xlsx'
    exclude_prefixes = [
        r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame/CDNRes/Rel_CDNUpload',
        r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame/CDNRes/Dev_CDNUpload'
    ]
    
    # 过滤路径并保存
    filter_paths(input_file, output_file, exclude_prefixes)
    
    print(f"文件已成功处理并保存到 {output_file}")