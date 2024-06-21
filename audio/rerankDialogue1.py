import json

# 读取JSON文件
with open('./output.json', 'r') as file:
    data = json.load(file)

# 解析文件A1，A2的数据
dialogue_A1 = data[1]['results'][0]['sentence_info']
dialogue_A2 = data[2]['results'][0]['sentence_info']

# 创建一个列表来保存所有的对话片段和对应的发言人
all_dialogues = []

# 将A1中的对话添加到列表中
for dialogue in dialogue_A1:
    all_dialogues.append({
        'start': dialogue['start'],
        'end': dialogue['end'],
        'text': dialogue['text'],
        'speaker': '客服'  # 假定A1是客服
    })

# 将A2中的对话添加到列表中
for dialogue in dialogue_A2:
    all_dialogues.append({
        'start': dialogue['start'],
        'end': dialogue['end'],
        'text': dialogue['text'],
        'speaker': '客户'  # 假定A2是客户
    })

# 按开始时间排序所有对话
all_dialogues.sort(key=lambda x: x['start'])

# 1.输出排序后的对话
for dialogue in all_dialogues:
    print(f"{dialogue['speaker']}({dialogue['start']}ms - {dialogue['end']}ms): {dialogue['text']}")


# 2.输出对话 -整合输出
def merge_consecutive_dialogues(dialogues):
    if not dialogues:
        return []

    merged_dialogues = []
    current_dialogue = dialogues[0].copy()

    for next_dialogue in dialogues[1:]:
        # 检查是否为同一发言人且时间连续
        if next_dialogue['speaker'] == current_dialogue['speaker'] and next_dialogue['start'] <= current_dialogue['end']:
            # 合并文本并更新结束时间
            current_dialogue['text'] += " " + next_dialogue['text']
            current_dialogue['end'] = next_dialogue['end']
        else:
            merged_dialogues.append(current_dialogue)
            current_dialogue = next_dialogue.copy()

    merged_dialogues.append(current_dialogue)
    return merged_dialogues

# 使用已经填充的all_dialogues列表
merged_dialogues = merge_consecutive_dialogues(all_dialogues)

# 输出合并后的对话
for dialogue in merged_dialogues:
    print(f"{dialogue['speaker']}({dialogue['start']}ms - {dialogue['end']}ms): {dialogue['text']}")