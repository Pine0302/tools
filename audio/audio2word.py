from funasr import AutoModel
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model = AutoModel(model="paraformer-zh",  
                  vad_model="fsmn-vad", 
                  vad_kwargs={"max_single_segment_time": 60000},
                  punc_model="ct-punc", 
                  # spk_model="cam++"
                  )
wav_file = "/home/pine/workspace/pythontool/audio/output/143822_057383693915_013588822626_m2gq059vdvkclkf03tdh.mp3"
res = model.generate(input=wav_file, batch_size_s=300, batch_size_threshold_s=60, hotword='魔搭')
print(res)