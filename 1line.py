import xml.etree.ElementTree as ET
import pandas as pd

def parse_svn_log(xml_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # 存储日志条目的列表
    log_entries = []
    
    # 遍历每个logentry元素
    for logentry in root.findall('logentry'):
        revision = logentry.get('revision')
        author = logentry.find('author').text
        date = logentry.find('date').text
        message = logentry.find('msg').text
        
        # 提取路径信息
        paths = []
        for path in logentry.findall('paths/path'):
            paths.append(f"{path.text} ({path.get('action')})")
        
        # 将日志条目添加到列表中
        log_entries.append({
            'Revision': revision,
            'Author': author,
            'Date': date,
            'Message': message,
            'Paths': paths
        })
    
    return log_entries

def save_to_excel(log_entries, excel_file):
    # 将日志条目列表转换为DataFrame
    df = pd.DataFrame(log_entries)
    
    # 展开Paths列，使其每个路径单独占一行
    df = df.explode('Paths')
    
    # 保存为Excel文件
    df.to_excel(excel_file, index=False)

# 主函数
if __name__ == "__main__":
    xml_file = 'log.xml'
    excel_file = 'svn_log.xlsx'
    
    # 解析XML文件
    log_entries = parse_svn_log(xml_file)
    
    # 保存为Excel文件
    save_to_excel(log_entries, excel_file)
    
    print(f"日志已成功保存到 {excel_file}")