from transformers import pipeline
import torch
import datetime
from pprint import pprint
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#1.自动问答,答案必须能在语料库中直接找到
#question_answerer = pipeline("question-answering") # bert-base
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/pytorch/question-answering/run_squad.py script.
"""
#需同时传入问题和语料库
#result = question_answerer(question="What is a good example of a question answering dataset?",context=context)
#print(result)

#2.文本分类
# classifier = pipeline("sentiment-analysis")
# result = classifier("I love you")[0]
# print(result)

#3.自动填空
# unmasker = pipeline("fill-mask")
# sentence = 'Huggingface is creating a <mask> that the comunity users to solve NLP tasks.'
# print(unmasker(sentence))

#4 文本生成(内容自动补全)
#text_generator = pipeline("text-generation") #gpt2
#print(text_generator("As far as I am concerned, I will",max_length=50,do_sample = False))

#5 命名实体识别
#ner = pipeline("ner",grouped_entites =  True)
#print(ner("My name is pine , and I work at Hugging Face in Brooklyn"))

#6 文本摘要
#summarizer = pipeline("summarization") # bart
ARTICLE = """ Jackie Chan is a renowned Hong Kong actor, martial artist, film director, and producer known for his unique blend of martial arts, action, and comedy. Born on April 7, 1954, in Hong Kong, Chan began his career as a child actor before rising to international fame with his acrobatic fighting style and innovative stunts. 
He gained recognition in the 1970s with movies such as "Drunken Master" and later achieved global success with hits like "Police Story," "Rumble in the Bronx," and "Rush Hour." His extensive filmography showcases his versatility, featuring both action-packed films and light-hearted comedies. Chan's contributions to the film industry have earned him numerous awards, including an Honorary Oscar for his achievements in cinema.
Beyond film, Chan is also a philanthropist, founding the Jackie Chan Charitable Foundation and actively supporting various charitable causes worldwide. His contributions to both cinema and society have solidified him as an international icon.
"""
#print(summarizer(ARTICLE,max_length=130,min_length=30,do_sample=False))

#7 自动翻译
""" translator = pipeline("translation_en_to_fr") # en,fr,de,ro
sentence = "Jackie Chan is a renowned Hong Kong actor"
print(translator(sentence,max_length=40))
 """

#8 中文文本分类（情感识别）
import sys
import os
# 获取当前文件的目录
current_path = os.path.dirname(__file__)
# 获取要导入的模块所在的目录
module_path = os.path.join(current_path, '../basic')
# 将模块的目录添加到sys.path中
sys.path.append(module_path)


#加载库和预训练模型
from transformers import AutoTokenizer #词模型
from transformers import AutoModelForSequenceClassification #预训练模型
from transformers import pipeline
from FileReader import FileReader

checkpoint = "IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment"
token = AutoTokenizer.from_pretrained(checkpoint) #词模型
model = AutoModelForSequenceClassification.from_pretrained(checkpoint) #预训练模型
text_class = pipeline("sentiment-analysis",model=model,tokenizer = token) #pipeline
print(text_class("这个产品用起来有点别扭"))
print(text_class("这个产品用起来还是挺舒适的有点别扭"))
print(text_class("这个产品用起来咋说呢，不太好描述"))