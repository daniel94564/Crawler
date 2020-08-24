#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import time as t
import datetime
import tkinter as tk
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import logging
import os
from pathlib import Path
import pyautogui

import configparser
from text_modules.get_location import get_location
from text_modules.get_comment_content import get_comment_content
from text_modules.get_post import get_post_content
from text_modules.get_comment_name import get_comment_name
from text_modules.get_product_info import get_product_info




config = configparser.ConfigParser()    # 注意大小寫
config.read("config.ini")   # 配置檔案的路徑

post_url=config['configs']['url']
comment_people_class=config['configs']['comment_people_class']
more_messages_xpath=config['configs']['more_messages_xpath']
post_content_class=config['configs']['post_content_class']
comment_class=config['configs']['comment_class']


wb = Workbook()
ws = wb.active

"""log紀錄"""
path = str(Path(os.getcwd()))
log_path = os.path.join(path,"log","info.log")

logging.basicConfig(level=logging.INFO,
					format='[%(asctime)-4s] %(message)s',
					datefmt='%Y-%m-%d %H:%M:%S',
					handlers = [logging.FileHandler(log_path, 'w+', 'utf-8'),])


def get_htmltext(username, password):
    global csv_lst
    comment_people_lst = []
    comment_lst = []
    product_lst = []
    quantity_lst=[]
    locat_lst = []

    chrome_options = Options()
    prefs = {
        'profile.default_content_setting_values' :
            {
            'notifications' : 1
            }
    } 

    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
#    driver位置,改路徑
    driver = webdriver.Chrome('/Users/cheer/Downloads/chromedriver',options=chrome_options)
    driver.get("http://www.facebook.com")
    t.sleep(3)
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)

    driver.find_element_by_id("u_0_b").click()
        
   
    t.sleep(3)
    url =post_url
    driver.get(url)
    t.sleep(5)
    


    try:
        driver.find_element_by_class_name('stjgntxs ni8dbmo4 g3eujd1d').click()
    except Exception as e:
        logging.info('無法關閉跳出視窗 : ' + str(e))
        pass

    
    


    #檢查有多少回覆或查看更多留言要按，少於10就停下來
#    while len(driver.find_elements_by_class_name('j83agx80 fv0vnmcu hpfvmrgz')) > 10:
#        clickN = driver.find_elements_by_class_name('j83agx80 fv0vnmcu hpfvmrgz')
#        print(len(clickN))
#        for i in range(len(clickN)):
#            clickN[i].click()

    # 點開所有留言

    print("點擊")
    try:
        driver.find_element_by_xpath(more_messages_xpath.click())
    except:
        print('No click')
    t.sleep(5)
        


    print("開始爬文")
    htmltext = driver.page_source
    soup = BeautifulSoup(htmltext,"lxml")
    

#    爬貼文
    post_content = soup.find(class_ = post_content_class).text
    
    post_type=get_post_content(post_content)[1]

   



#    找留言者
    comment_people = soup.find_all(class_ = comment_people_class) # 留言人
    for comment_person in comment_people:
        comment_people_lst.append(get_comment_name(comment_person.text,post_type))


    comments = soup.find_all('div',class_ = comment_class) # 留言


    for comment in comments:
        comment_lst.append(get_comment_content(comment.text,post_type))
        product_lst.append(get_product_info(comment.text,post_type))
        print(get_product_info(comment.text,post_type))
        quantity_lst.append(get_product_info(comment.text,post_type))
        locat_lst.append(get_location(comment.text))


    csv_lst.append(['文章連結', '文章內容', '留言人', '留言', '商品', '取貨地點','價錢'])
    csv_lst.append([url, get_post_content(post_content)[0], comment_people_lst[0], comment_lst[0], product_lst[0], locat_lst[0]])
    for i in range(1, len(comment_people_lst)):
        csv_lst.append(['', '', comment_people_lst[i], comment_lst[i], product_lst[i],locat_lst[i]])

    driver.close()
    To_csv(len(comment_people_lst))

"""設定CSV的欄位標題"""
def writePandas(data_lst):
    df = pd.DataFrame(data=csv_lst, columns=['文章連結', '文章內容', '留言人', '留言', '商品', '取貨地點','價錢'])
    return df

"""將存取的資料轉成CSV格式輸出"""
def To_csv(column_length):
    global csv_lst
    fileName = '乖寶嚴選_' + t.strftime('%Y%m%d%H%M%S', t.localtime())
    try:
        with open('data/xls/'+fileName+'.xlsx', 'w') as new_csv:
            pass
        df = writePandas(csv_lst)
        df.sort_values(by='取貨地點')
        df_lst = df.values.tolist()
        
        for r in df_lst:
            ws.append(r)
            
        ws.auto_filter.ref = "C1:F" + str(column_length)
        ws.auto_filter.add_filter_column(0, [''])
        wb.save('data/xls/'+fileName+'.xlsx')

    except Exception as e:
        logging.info('程式異常 : ' + str(e))
        pass

    csv_lst = []


if __name__ == '__main__':
    username = config['configs']['acc']
    password = config['configs']['pwd']

    csv_lst = []
    htmltext = get_htmltext(username, password)
