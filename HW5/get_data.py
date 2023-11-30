# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:00:12 2023

@author: sophie
"""
import datetime
import time
import random
import os.path
import json
import requests
from bs4 import BeautifulSoup

headers = {
    # 使用者代理
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.124 Safari/537.36",
    "Referer": "https://www.google.com/"  # 參照位址
}

# 輸出路徑檔案
cur_path = os.path.dirname(__file__)
output_file = os.path.abspath('sophie_prac.json')
output2_file = os.path.abspath('sophie_prac.txt')

# url 李宗盛歌曲專區
url='https://mojim.com/twh100041-A2.htm'
web_url='https://mojim.com'

# test1
content_txt = ''
html = requests.get(url, headers=headers)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'html.parser')

# 李宗盛專區內有多少曲目
spansLength=len(sp.select('.hc1'))

for i in range(1,spansLength):

    span=sp.select('.hc1')[i]
    span_href=span.find('a').get('href')
    span_title=span.find('a').get('title')[:-3]
    # 取出單曲的網址
    lyrics_url=web_url + span_href

    # 終端機顯示處理進度
    print (i)
    print(span_title)
    print(lyrics_url)

    # 進入單曲抓歌詞
    html_2 = requests.get(lyrics_url, headers=headers)
    html_2.encoding = 'UTF-8'
    sp_2 = BeautifulSoup(html_2.text, 'html.parser')
    lyrics=sp_2.select_one('.fsZx3')
    lyrics_txt=lyrics.text

    # 存入txt
    with open(output2_file, 'a+', encoding='utf-8') as temp2:
        temp2.write(' ' +  lyrics_txt + '\n')
        temp2.close()

    # 隨機延遲，以免被網站擋
    delay_choices = [8, 5, 10, 6, 20, 11]  # 延遲的秒數
    delay = random.choice(delay_choices)  # 隨機選取秒數
    time.sleep(delay)  # 延遲



