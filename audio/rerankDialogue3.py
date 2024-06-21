import json
from difflib import SequenceMatcher

### 以全对话文件为基准,去匹配左右对话的文字
# 优点:对话顺序好,逻辑对
# 缺点:匹配不到有未知的情况
# 读取JSON文件
with open('./output.json', 'r') as file:
    data = json.load(file)

dialogue_A = data[0]['results'][0]['sentence_info']
dialogue_A1 = data[1]['results'][0]['sentence_info']
dialogue_A2 = data[2]['results'][0]['sentence_info']

def preprocess_text(text):
    return text.replace("嗯", "").replace("啊", "").replace("。", "").strip()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()



def find_speaker(dialogue, dialogue_A1, dialogue_A2, tolerance=600):
    max_similarity = 0.8  # 初始化最大相似度
    speaker = "未知"  # 初始化发言人为未知

    # 检查A1中的匹配项
    for entry in dialogue_A1:
        current_similarity = similar(preprocess_text(dialogue['text']), preprocess_text(entry['text']))
        if abs(dialogue['start'] - entry['start']) <= tolerance and current_similarity > max_similarity:
            max_similarity = current_similarity
            speaker = "客服"  # A1通常代表客服

    # 检查A2中的匹配项
    for entry in dialogue_A2:
        current_similarity = similar(preprocess_text(dialogue['text']), preprocess_text(entry['text']))
        if abs(dialogue['start'] - entry['start']) <= tolerance and current_similarity > max_similarity:
            max_similarity = current_similarity
            speaker = "客户"  # A2通常代表客户

    return speaker

all_dialogues = []
for dialogue in dialogue_A:
    speaker = find_speaker(dialogue, dialogue_A1, dialogue_A2)
    dialogue['speaker'] = speaker
    all_dialogues.append(dialogue)

#print(all_dialogues)
# 1.输出对话 -离散输出
for dialogue in all_dialogues:
     print(f"{dialogue['speaker']}({dialogue['start']}ms - {dialogue['end']}ms): {dialogue['text']}")

# 1.输出对话 -整合输出
# def merge_consecutive_dialogues(dialogues):
#     if not dialogues:
#         return []

#     merged_dialogues = []
#     current_dialogue = dialogues[0].copy()

#     for next_dialogue in dialogues[1:]:
#         # 检查是否为同一发言人且时间连续
#         if next_dialogue['speaker'] == current_dialogue['speaker'] and next_dialogue['start'] <= current_dialogue['end']:
#             # 合并文本并更新结束时间
#             current_dialogue['text'] += " " + next_dialogue['text']
#             current_dialogue['end'] = next_dialogue['end']
#         else:
#             merged_dialogues.append(current_dialogue)
#             current_dialogue = next_dialogue.copy()

#     merged_dialogues.append(current_dialogue)
#     return merged_dialogues

# # 使用已经填充的all_dialogues列表
# all_dialogues = sorted(all_dialogues, key=lambda x: x['start'])
# merged_dialogues = merge_consecutive_dialogues(all_dialogues)

# # 输出合并后的对话
# for dialogue in merged_dialogues:
#     print(f"{dialogue['speaker']}({dialogue['start']}ms - {dialogue['end']}ms): {dialogue['text']}")
