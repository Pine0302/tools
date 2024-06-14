from gensim.models import word2vec,Word2Vec
from functools import reduce
import chardet
import jieba.analyse
import numpy as np
import pandas as pd
import sqlalchemy
import sqlite3
import argparse
import sys
import os
import re
import logging
# 获取当前文件的目录
current_path = os.path.dirname(__file__)

# 获取要导入的模块所在的目录
module_path = os.path.join(current_path, '../basic')

# 将模块的目录添加到sys.path中
sys.path.append(module_path)
logging.basicConfig(filename='/home/pine/workspace/pythontool/test1.txt', level=logging.INFO)
from FileReader import FileReader
from FileLister import FileLister
class Word2vecs:
    def __init__(self, name):
        self.name = name
    
    def normalWord2vecs(self,file_content, topK=20, withWeight=False, allowPOS=()):
        return 
    
    def modelExec(self,model_name):
        new_model= Word2Vec.load(model_name)
        #print(new_model.wv.key_to_index)
        #print(new_model.wv.most_similar("中国",topn=20))
        print(new_model.wv.most_similar(negative = "不好",topn=20))


    def filterContent(self,file_content):
        # 定义要删除的字符串模式
        patterns_to_remove = [r"\u3000", r"&nbsp;", r"&nbsp", r"\t"]  # 你要删除的字符串模式列表
        for pattern in patterns_to_remove:
            file_content = re.sub(pattern, "", file_content)
        return file_content    

    def main(self, args):
        print(f"接收到的参数是: {args.dir_path}")
        #文件列表读取
        fileList = FileLister(args.dir_path)
        files = fileList.list_files()
        
        #获取停用词
        stop_words_path = "/home/pine/workspace/resource/stopwords/cn_stopwords.txt"
        stop_words_set = set()
        with open(stop_words_path, "r", encoding="utf-8") as f:
            for line in f:
                stop_words_set.add(line.strip())     
        all_words_flattened = []
        if files:
            for file in files:
                #print(f"读取的文件是: {file}")
                reader = FileReader(file)
                file_content = reader.read()
                if file_content is not None:
                    file_content = self.filterContent(file_content)
                    segment_lines = re.split(r'[。!？\n]',file_content)
                    #print(segment_lines)
                    string_list = [''.join([sentence for sentence in sublist if sentence]) for sublist in segment_lines if any(sublist)]
                else:
                    os.remove(file)    
                # 对每个句子进行中文分词，并将分词结果存储在一个新的列表中
                #all_words = [jieba.lcut(sent, cut_all=False) for sent in string_list]
                all_words = [jieba.lcut(sent) for sent in string_list]
                words_without_stopwords = [[word for word in sentence if word not in stop_words_set] for sentence in all_words]
                all_words_flattened.extend(all_words)
                # 将分词结果展开，存储在一个新的列表中
                """ all_words_flattened = [word for sublist in all_words for word in sublist]
                words_without_stopwords = [word for word in all_words_flattened if word not in stop_words_set]
                logging.info(words_without_stopwords) """
            w2v_model = word2vec.Word2Vec(all_words_flattened,vector_size = 150,window = 10,min_count=2,sg=1)
            w2v_model.save("Pine_w2v_model")
            print(w2v_model.wv.key_to_index)
        else:
            print("没有找到文件")

        self.modelExec("Pine_w2v_model")
        

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="文本向量化python脚本示例")
    parser.add_argument('-dir', '--dir_path', type=str, help='传入的文件夹地址', default='默认信息')

    #file_content = "这是一个示例。这是第二个示例！这是第三个示例？这是第四个示例。\n这是第五个示例。"

    #sentences = re.split(r'[。!？\n]', file_content)

    #print(sentences)
    # 解析参数
    args = parser.parse_args()

    # 创建类的实例并调用main函数
    word2vecs = Word2vecs("word2vecs")
    word2vecs.main(args)
