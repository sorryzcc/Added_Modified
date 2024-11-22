import xml.etree.ElementTree as ET
import csv

def parse_svn_log(xml_file, csv_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # 打开CSV文件准备写入
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['revision', 'author', 'date', 'message', 'paths']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 写入CSV文件头
        writer.writeheader()
        
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
            paths_str = '; '.join(paths)
            
            # 写入行数据
            writer.writerow({'revision': revision, 'author': author, 'date': date, 'message': message, 'paths': paths_str})

# 调用函数
parse_svn_log('log.xml', 'svn_log.csv')