#### 目標網站選擇說明
[鉅亨網](https://cnyes.com)，是個介紹財經相關訊息的網站，因為呈現新聞訊息的瀏覽方式為 {主網址}+/id/新聞編號，對初學爬蟲者較易學習，寫迴圈就可以取得若干訊息，以作為文字雲的素材。不用動到selenium更複雜的設定及寫法，惟僅靠class以及beautifulSoup選擇，可能仍無法精確的鎖定訊息的類別。如果未來還要再爬相關資料的話，目前大多數的財經網站，大多數為滾動式分頁，恐怕還是得花時間使用selenium。

  ##### 鉅亨網爬蟲程式許可行為宣告
  [原始檔案](https://news.cnyes.com/robots.txt)
  已另存到/resources/cnyes_com_robots.txt，看起來本次的操作沒有在"Disallow"的範圍內

#### 操作步驟
  ##### 安裝套件 本次需要用到 beautifulSoup(bs4), WordCloud, PIL(pillow), os_path, jieba...等等套件，需要用 pin3 install 先安裝備用

  ##### 資料爬蟲 程式詳見 "./get_data.py"
  看了幾則新聞後，發現 class='_2E8y'的文章似乎比較符合爬取的方向。原先設定擷取100篇，但原網站有日期限制，僅取得80餘篇資料，並存成.txt 或 .json備用。

  ##### 結巴分詞
  中英文的分詞原則不同，下載目前有先進已開發的 dict.txt 及 stopword.txt 備用

  ##### 文字雲計算及繪圖
  因為wordcloud似乎不接受相對路徑，記得用os.path.join把相關檔案串成完整的絕對路徑。
  為免圖的項目過雜，僅取出前25名出現頻率最多的來製圖。
  其他依照先進的方式，將相關的參數放到適當的位置，執行後即所的文字雲圖。


#### 參考資料
1.[Python爬蟲教學]7個降低Python網頁爬蟲被偵測封鎖的實用方法
https://www.learncodewithmike.com/2020/09/7-tips-to-avoid-getting-blocked-while-scraping.html

2.擷取上一頁a標籤裡的網址來GET上一頁的網頁
https://ithelp.ithome.com.tw/articles/10202493

3.Python判断字符串是否为空和null
https://cloud.tencent.com/developer/article/1738542

4.文字檔案讀取/寫入
https://ithelp.ithome.com.tw/articles/10202725

5.以utf-8寫入以避免亂碼
https://stackoverflow.com/questions/18337407/saving-utf-8-texts-with-json-dumps-as-utf-8-not-as-a-u-escape-sequence

6.絕對路徑拼接
https://zhuanlan.zhihu.com/p/105643655

7.如何使用 jieba 結巴中文分詞程式
https://coderwall.com/p/38wtgw/jieba

8.如何使用 Python 製作文字雲
https://tech.havocfuture.tw/blog/python-wordcloud-jieba



