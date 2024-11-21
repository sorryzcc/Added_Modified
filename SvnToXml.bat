import xml.etree.ElementTree as ET
import csv

def parse_svn_log_xml(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    rows = []

    for logentry in root.findall('logentry'):
        revision = logentry.attrib['revision']
        author = logentry.find('author').text
        date = logentry.find('date').text
        msg = logentry.find('msg').text

        for path in logentry.find('paths').findall('path'):
            if path.text.endswith('.png'):
                action = path.attrib['action']
                rows.append([path.text, date, action])

    # 写入CSV文件
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['路径', '时间', 'A/M'])  # 写入表头
        writer.writerows(rows)  # 写入数据行

# 使用方法
xml_file = 'log.xml'  # 你的XML日志文件路径
output_file = 'output.csv'  # 输出的CSV文件名
parse_svn_log_xml(xml_file, output_file)

print(f"处理完成，输出已保存至 {output_file}")