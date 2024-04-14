import chardet
import jieba.analyse
import numpy as np
import pandas as pd
import sqlalchemy
import sqlite3
import argparse
import sys
import os

# 获取当前文件的目录
current_path = os.path.dirname(__file__)

# 获取要导入的模块所在的目录
module_path = os.path.join(current_path, '../basic')

# 将模块的目录添加到sys.path中
sys.path.append(module_path)

# 现在可以导入模块了
from FileReader import FileReader
class TextExtract:
    def __init__(self, name):
        self.name = name
    
    def extractTextTfIdf(self,file_content, topK=20, withWeight=False, allowPOS=()):
        #普通模式
        #jieba默认加载自己的idf，我们可以加载自带idf文件
        jieba.analyse.set_idf_path("/home/pine/anaconda3/envs/ai/lib/python3.10/site-packages/jieba/analyse/idf.txt")
        return jieba.analyse.extract_tags(file_content, topK, withWeight, allowPOS)

    def extractTextRank(self,file_content, topK=20, withWeight=False, allowPOS=()):
        #普通模式
        #jieba默认加载自己的idf，我们可以加载自带idf文件
        jieba.analyse.textrank(file_content,topK=20,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
        return jieba.analyse.extract_tags(file_content, topK, withWeight, allowPOS)

    def main(self, args):
        print(f"接收到的参数是: {args.file_path}")
        #文章读取
        reader = FileReader(args.file_path)
        file_content = reader.read()
        print(f"读取的文章是: {file_content}")
        #获取关键词
        print(self.extractTextTfIdf(file_content,allowPOS=("n")))
        print(self.extractTextRank(file_content))

        

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="文件信息抽取python脚本示例")
    parser.add_argument('-file', '--file_path', type=str, help='传入的文件地址', default='默认信息')

    # 解析参数
    args = parser.parse_args()

    # 创建类的实例并调用main函数
    textExtract = TextExtract("textExtract")
    textExtract.main(args)
