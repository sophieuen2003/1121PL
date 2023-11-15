#encoding=utf-8
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import jieba.analyse
from collections import Counter
import os.path

cur_path = os.path.dirname(__file__)
resource_path = os.path.join(cur_path,'resources')


dictFile = os.path.join(resource_path,'dict.txt')  # 字典檔
stopFile = os.path.join(resource_path,'stopwords.txt')  # stopwords
fontPath =os.path.join(resource_path,'DFT_C3.ttc')  # 字型檔

myFile = os.path.join(cur_path,'sophie_prac.txt')

# jieba
jieba.set_dictionary(dictFile)
jieba.analyse.set_stop_words(stopFile)
text=open(myFile,"r",encoding='utf-8').read()
tags=jieba.analyse.extract_tags(text,topK=25)

segList=jieba.lcut(text,cut_all=False)
dictionary=Counter(segList)

freq={}
for ele in dictionary:
  if ele in tags:
    freq[ele]=dictionary[ele]
print(freq)

## wordCloud
# mask
x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

# Generate a word cloud image
wordcloud = WordCloud(background_color="white", mask=mask, contour_width=3, contour_color='steelblue', font_path=fontPath).generate_from_frequencies(freq)

# 繪圖
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()





