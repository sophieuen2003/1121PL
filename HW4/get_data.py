# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:18:12 2023

@author: sophie
"""
import datetime
import time
import random
import os.path
import json
import requests
from bs4 import BeautifulSoup
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-TW,zh;q=0.9",
#     "Host": "news.cnyes.com",  # 目標網站
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Upgrade-Insecure-Requests": "1",
#     # 使用者代理
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.124 Safari/537.36",
#     "Referer": "https://www.google.com/"  # 參照位址
# }
headers ={
    "content-type": "text/html; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/119.0.6045.124  Safari/537.36"
}


# 輸出路徑檔案
cur_path = os.path.dirname(__file__)
output_file = os.path.abspath('sophie_prac.json')
output2_file = os.path.abspath('sophie_prac.txt')



# url
# id = 5377884  # 目前作業id，初始值為21286最新一筆
id = 5381657  # 目前作業id，初始值為21286最新一筆
url_init = 'id/'+str(id)+'?exp=a'
url_h = 'https://news.cnyes.com/news/'
# https://news.cnyes.com/news/id/5377884?exp=a

# 抓100次
for i in range(100):

    url_init = 'id/'+str(id)+'?exp=a'
    url = url_h + url_init
    html = requests.get(url, headers=headers)
    html.encoding = 'UTF-8'
    sp = BeautifulSoup(html.text, 'html.parser')

    # 找class='_2E8y'的文章
    article_idv=sp.select('._2E8y')[0]
    # article_idv=sp.select('.')[0]
    # print('--------------------------------')
    # print(article_idv)
    # print('--------------------------------')
    content_txt = ''

    if bool(article_idv):

        print('第' + str(i) + '筆' + '-'*15)
        print(datetime.datetime.today())
        print(url)
        # print('article_idv_2:',article_idv)

        # 準備二次過濾tag
        article_idv_txt = BeautifulSoup(article_idv.text,'html.parser')
        content_txt += str(article_idv_txt)+' \n'

        print('content_txt:',content_txt)
        # 設定成json格式
        json1 = {
            "id": id,
            # "post_date": post_date,
            # "title": title_txt,
            "content": content_txt
        }

        # 存入json
        with open(output_file, "r+", encoding='utf-8') as temp1:
            data_j = json.load(temp1)
            data_j.append(json1)
            temp1.seek(0)

            json.dump(data_j, temp1, ensure_ascii=False)

        # 存入txt
        with open(output2_file, 'a+', encoding='utf-8') as temp2:
            # temp2.write('序號：'+str(id)+'\n')
            # temp2.write('發佈日期：' + post_date + '\n')
            # temp2.write('主題：' + title_txt + '\n')
            # temp2.write('內容：' + content_txt + '\n')
            temp2.write(' ' + content_txt + '\n')
            temp2.close()

        delay_choices = [8, 5, 10, 6, 20, 11]  # 延遲的秒數
        delay = random.choice(delay_choices)  # 隨機選取秒數
        time.sleep(delay)  # 延遲

    id-=1
