import os
import sys
import json

from funasr import AutoModel

# # 获取当前文件的目录路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 获取当前目录的父目录，假设 audio_handler 在该目录下
# parent_dir = os.path.dirname(current_dir)
# # 将父目录添加到 sys.path
# sys.path.append(parent_dir)

from audio_handler.audio_handler import split_stereo_channels, convert_mp3_to_wav

# 文件路径配置
origin_audio_file = "/home/pine/workspace/pythontool/audio/output/143822_057383693915_013588822626_m2gq059vdvkclkf03tdh.mp3"
output_directory = os.path.dirname(origin_audio_file)
base_filename = os.path.splitext(os.path.basename(origin_audio_file))[0]

# 1. 将MP3文件转换为WAV格式
wav_file = os.path.join(output_directory, f"{base_filename}.wav")
convert_mp3_to_wav(origin_audio_file, wav_file)

# 2. 分离左右声道
left_channel_file = f"{base_filename}_left.wav"
right_channel_file = f"{base_filename}_right.wav"
split_stereo_channels(wav_file, output_directory, left_channel_file, right_channel_file)

# 完整路径
left_channel_path = os.path.join(output_directory, left_channel_file)
right_channel_path = os.path.join(output_directory, right_channel_file)


# 3. 初始化模型
local_model_path = "/home/pine/workspace/models/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
local_vad_model_path = "/home/pine/workspace/models/speech_fsmn_vad_zh-cn-16k-common-pytorch"
local_punc_model_path = "/home/pine/workspace/models/punc_ct-transformer_zh-cn-common-vocab272727-pytorch"
local_cam_model_path = "/home/pine/workspace/models/speech_campplus_sv_zh-cn_16k-common"

model = AutoModel(model=local_model_path,  model_revision="v2.0.4",
                   vad_model=local_vad_model_path, 
                   vad_model_revision="v2.0.4",
                   punc_model=local_punc_model_path,punc_model_revision="v2.0.4",
                   spk_model=local_cam_model_path,
                   )

#识别和输出
# 创建一个列表用于存放每个文件及其处理结果
output_data = []

# 4. 对每个文件进行语音识别
files_to_process = [wav_file, left_channel_path, right_channel_path]
results = {}
for file in files_to_process:
    res = model.generate(input=file, batch_size_s=300, hotword='魔搭')
    results[file] = res
    # 打印结果
for file, result in results.items():
    output_data.append({
    'file': file,
    'results': result
        })
    print(f"Results for {file}:")
    print(result)

# 转换为 JSON 格式字符串
json_output = json.dumps(output_data, ensure_ascii=False, indent=4)

# 打开一个文件用于写入，如果文件不存在则创建
with open('output.json', 'w') as file:
    file.write(json_output)  # 将字符串写入文件

print("输出已保存到文件 output.json")


       



        