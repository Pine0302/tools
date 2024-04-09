from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#获取url数据
url = 'http://njua.pinecc.cn/model/DPAEF-AbnormalRecognition.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# 假设评论在一个特定的HTML标签内，比如<div class="review">，需要根据实际网页结构调整
reviews = soup.find_all('span', class_='')
# 提取评论文本
comments = [review.get_text() for review in reviews]
#print(comments)

# 清洗数据，移除不需要的字符
cleaned_comments = [re.sub(r'[^\w\s]', '', comment) for comment in comments]
cleaned_comments = [re.sub(r'\s+', ' ', comment).strip() for comment in cleaned_comments]

#结巴分词
font_path = '/home/pine/.fonts/SimHei.ttf'
df = pd.DataFrame(cleaned_comments, columns=['Comment'])
df['Segmented'] = df['Comment'].apply(lambda x: ' '.join(jieba.cut(x)))

#词云生成
# 将所有评论合并成一个长字符串
text = ' '.join(df['Segmented'])
# 创建词云对象，指定字体路径（如果需要显示中文）
wordcloud = WordCloud(font_path=font_path).generate(text)
# 显示词云
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show() 