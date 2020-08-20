#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:40 2020

@author: cheer
"""

std_sample_text='羅焌輔管理員  · ==========7月6日======  · @傳統意麵雞絲麵@10顆一組團購價A:意麵＋1＝99元 / ＋5＝350元B:雞絲麵 ＋1＝99元 / ＋5＝350元＋1就是10顆一組了喔，＋5整箱50顆批發價給大家喔這個方便又好吃喔之前去吃火鍋，順手放一包下去煮，終於知道為什麼這家都要排隊了！麵煮了不會爛，麵本身也有鹹度，又香！又好吃難怪這麼夯～～～意麵 #再升級，選用更好的麵粉#口感更扎實，經實驗證明更不容易軟爛堅持 #天然無添加化學物堅持 #福懋植物油品堅持 #每天檢驗油品酸價值堅持 #機具環境保持乾淨整潔消夜 早餐都很讚 保存期限：意麵6個月，雞絲麵3個月 最新效期12123333'


def get_post_content(post):
    start_end_token=[]
    case_type=0
    for i in range(len(post)):
        if post[i]=='@':
            start_end_token.append(i)
            case_type=1
    
    return(post[start_end_token[0]+1:start_end_token[1]],case_type)
    
print(get_post_content(std_sample_text))

