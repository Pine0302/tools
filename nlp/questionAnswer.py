import transformers
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
from transformers import AutoModelForQuestionAnswering #预训练模型
from transformers import pipeline
from FileReader import FileReader



checkpoint = "luhua/chinese_pretrain_mrc_macbert_large"

token = AutoTokenizer.from_pretrained(checkpoint) #词模型
model = AutoModelForQuestionAnswering.from_pretrained(checkpoint) #预训练模型

question_answer = pipeline("question-answering",model=model,tokenizer = token) #pipeline

#加载语料库
file_name = "/home/pine/Downloads/CN_Corpus/CN_Corpus/SogouC.reduced/Reduced/C000008/10.txt"
reader = FileReader(file_name)
cont = reader.read()

#自动问答
result = question_answer(question = input(),context = cont)
print(result['answer'])