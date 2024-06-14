### 这是一个小脚本，用来完成截图后OCR识别复制到系统剪切板的功能

- 识别截图的方法应该可以使用一些截图工具自带的脚本关联，我采用了监控截图保存目录的文件变动的方案
- ocr识别我采用方案是薅一下百度api的羊毛，可以使用pytesseract等一些插件，识别精度不高（可以先优化图片再识别，但是比起百度api还是差点）
- 可以配置ubuntu自启动，研究下crontab -e 的 @restart 可以解决，不过crontab下要解决一些问题（环境变量获取，复制的时候获取不到display框：export DISPLAY=:0 等问题）
- ubuntu下的微信真垃圾，截图之后复制到对话框里面都不行，所以也不知道微信看图识字能不能用，干脆自己整理了这个方案

## nlp-extractText：
```
python extractText.py -file "/home/pine/Downloads/CN_Corpus/CN_Corpus/SogouC.reduced/Reduced/C000008/11.txt"
```
###
```
from gensim.models import word2vec,Word2Vec
#生成模型
python word2vecs.py -dir "/home/pine/Downloads/CN_Corpus/CN_Corpus/SogouC.reduced/Reduced/C000020"
#调试模型
python word2vecs.py
```