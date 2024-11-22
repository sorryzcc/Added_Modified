import pandas as pd

def deduplicate_excel(input_file, output_file):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 确保列名正确
    if 'A' in df.columns:
        df.rename(columns={'A': 'Action'}, inplace=True)
    
    # 对Path列进行去重，保留第一次出现的记录，并保留Action列
    df = df.drop_duplicates(subset=['Path'], keep='first')
    
    # 保存为新的Excel文件
    df.to_excel(output_file, index=False)

# 主函数
if __name__ == "__main__":
    input_file = '去除了删除的.xlsx'
    output_file = '去重后的文件.xlsx'
    
    # 去重并保存
    deduplicate_excel(input_file, output_file)
    
    print(f"文件已成功去重并保存到 {output_file}")