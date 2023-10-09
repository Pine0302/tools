import os
import json

# 把问题和答案组装成json格式集中存储到某个文件中
# {"question": "查看SGA和PGA大小\n", "answer": ["\n", "#查看SGA大小：\n", "\n", "show parameter sga\n", "\n", "查看PGA大小：\n", "\n", "show parameter pga\n"]}
# {"question": "数据库会话数统计\n", "answer": ["\n", "select status, count(\\*) from v\\$session group by status;\n"]}
filepath = '/home/pine/workspace/model/tempFile/md1'
destination_path = '/home/pine/workspace/model/tempFile/tt.json'

# 清空json文件
cmd = "echo '' > /home/pine/workspace/model/tempFile/tt.json"
os.system(cmd)

file_names = os.listdir(filepath)
for file_name in file_names:
    with open(filepath + "/" + file_name, 'r') as f:
        lines = f.readlines()
        answer = ''
        question = lines[0].replace('\n', '')
        lines.pop(0)
        if question == '问题描述' or question == "问题描述:":
            question = lines[1]
            lines.pop(0)
        q_plus = 0
        for i in range(0, len(lines)):
            if lines[i] == '\n':
                pass
            elif lines[i] == '问题描述' or lines[i] == "问题描述:" or lines[i] == "问题描述\n" or lines[i] == "问题描述：\n" or lines[
                i] == "问题描述:\n":
                n = 1
                while n <= 3:
                    if lines[i + n] != '\n':
                        q_plus = i + n
                        question += ': ' + lines[i + n]
                        n = 6
                    n += 1
            elif lines[i].find('问题描述') != -1:
                question += ': ' + lines[i]
            else:
                if i != q_plus:
                    answer = answer + ' ' + lines[i]
        dict_lines = {"question": question, "answer": answer}
        with open(destination_path, 'a') as file_obj:
            file_obj.write('\n')
            json.dump(dict_lines,file_obj, ensure_ascii=False)

        # for line in lines:
        #     if line == '\n':
        #         # print('empty line')
        #     elif line == '问题描述' or line == "问题描述:" or line == "问题描述\n" or line == "问题描述：\n" or line == "问题描述:\n":
        #         print("--:" + line)
        #         print("old_question:" +question)
        #     else:
        #         # answer = answer + line.replace('\n', ' ')
        #         answer = answer + ' ' + line
        # print(answer)
