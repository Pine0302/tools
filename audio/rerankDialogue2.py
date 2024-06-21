import json

### 以左右声道为基准匹配源对话
# 优点:不会有未知的情况
# 缺点:有些对话切割不好,顺序不对
# 读取JSON文件
with open('./output.json', 'r') as file:
    data = json.load(file)

# 解析文件A，A1，A2的数据
dialogue_A = data[0]['results'][0]['sentence_info']
print(dialogue_A)
dialogue_A1 = data[1]['results'][0]['sentence_info']
print(dialogue_A)
dialogue_A2 = data[2]['results'][0]['sentence_info']

# 容差值（毫秒）
tolerance = 600

# 创建一个列表来保存所有的对话片段和对应的发言人
all_dialogues = []

def match_words(source_sentence, target_sentence, tolerance=600):  # 增加默认容差
    # 检查每个单词时间戳是否在容差范围内
    for word_info in source_sentence['timestamp']:
        for target_word_info in target_sentence['timestamp']:
            if abs(word_info[0] - target_word_info[0]) <= tolerance and abs(word_info[1] - target_word_info[1]) <= tolerance:
                return True
    return False

def add_dialogues(source, speaker, dialogue_A, all_dialogues):
    for dialogue in source:
        matched = False
        # 寻找时间匹配的对话
        for entry in dialogue_A:
            if abs(dialogue['start'] - entry['start']) <= tolerance and abs(dialogue['end'] - entry['end']) <= tolerance:
                if match_words(dialogue, entry):  # 精确匹配每个字的时间戳
                    matched = True
                    break
        if not matched:
            print(f"Matching failed for: {dialogue['text']} at {dialogue['start']} to {dialogue['end']}")
        all_dialogues.append({
            'start': dialogue['start'],
            'end': dialogue['end'],
            'text': dialogue['text'],
            'speaker': speaker
        })

all_dialogues = []
add_dialogues(dialogue_A1, '客服', dialogue_A, all_dialogues)
add_dialogues(dialogue_A2, '客户', dialogue_A, all_dialogues)

# 输出对话
all_dialogues = sorted(all_dialogues, key=lambda x: x['start'])
for dialogue in all_dialogues:
    print(f"{dialogue['speaker']}({dialogue['start']}ms - {dialogue['end']}ms): {dialogue['text']}")