import os
import json

#把问题和答案组装成json格式集中存储到某个文件中
#{"question": "查看SGA和PGA大小\n", "answer": ["\n", "#查看SGA大小：\n", "\n", "show parameter sga\n", "\n", "查看PGA大小：\n", "\n", "show parameter pga\n"]}
#{"question": "数据库会话数统计\n", "answer": ["\n", "select status, count(\\*) from v\\$session group by status;\n"]}
filepath = '/home/pine/workspace/model/tempFile/md'
destination_path = '/home/pine/workspace/model/tempFile/result.json'

file_names = os.listdir(filepath)
for file_name in file_names:
    with open(filepath+"/"+file_name, 'r') as f:
        lines = f.readlines()
        dict_lines = {"question": lines[0], "answer": lines[1::1]}
        print(dict_lines)
        with open(destination_path, 'a') as file_obj:
            file_obj.write('\n')
            json.dump(dict_lines,file_obj, ensure_ascii=False)
