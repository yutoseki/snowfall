#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install selenium
# !pip install beautifulsoup4


# In[2]:


from selenium import webdriver
import time
import pandas as pd
import os
import datetime
from selenium.webdriver import ChromeOptions 
from selenium.webdriver.chrome.webdriver import WebDriver
import glob
import time
import shutil
from bs4 import BeautifulSoup
import urllib.request as req


# In[3]:


# タングラムスキーサーカス
url1 ="https://www.tangram.jp/ski/ski/lift.php"
response1=req.urlopen(url1)
# 蓼科東急スキー場
url2 ="https://www.tateshina-tokyu.com/ski/"
response2=req.urlopen(url2)
# スキージャム勝山
url3 ="https://www.skijam.jp/winter/gelande/"
response3=req.urlopen(url3)
# ダイナランド
url4 ="https://www.dynaland.co.jp/"
response4=req.urlopen(url4)


# In[4]:


parse_html1= BeautifulSoup(response1,'html.parser')
parse_html2= BeautifulSoup(response2,'html.parser')
parse_html3= BeautifulSoup(response3,'html.parser')
parse_html4= BeautifulSoup(response4,'html.parser')


# In[5]:


#　コンテンツの大元のリスト作成
parse_html_lists = [parse_html1,parse_html2,parse_html3,parse_html4]


# In[6]:


# タイトルとコンテンツの一括取得
i=0
content_lists = []
class_lists = ['lift list','liveinfo_box','pc','hide course_content']
for parse_html_list in parse_html_lists:
    print("-----------------------------------------------------")
    print(parse_html_lists[i].title.string)
    content_lists.append(parse_html_list.find(class_=class_lists[i]))
    print(content_lists[i].text)
    i += 1
    print("-----------------------------------------------------")


# In[ ]:




