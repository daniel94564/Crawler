#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:16:14 2020

@author: cheer
"""
post='^韓風正式吹來啦!!! 韓國知名大廠SAMJIN AMOOK助陣^ 品名: A.青陽辣椒魚板:400克/包(10串)~ B.包心年糕魚板捲:520克/包(10串)~ C.海鮮魚板條:400克/包(10串)~ D.香菇魚板條:400克/包(10串)~ E.蔬菜魚板片:400克/包(10串)~ F.傳統魚板片:320克/包(10串)~ G.魷魚魚板樹:500克/包(10串)~ H.三角冬粉魚板片:400克/包(10串)~ I.蟹肉風味魚板:400克/包(10串)~ 團購價＋1＝110元 / ＋3＝300元! 你從未吃過的高級韓國魚板 韓國連鎖餐廳一支就要30 40元 真的超級好吃!! 超級好吃!! 超級好吃～～～～～～ 中秋限定 各個口味數量有限 以先出貨為主要搶要快啊!! 讓各位也能品嘗原汁原味的韓式飲食!!! 這次推出超多種口味的魚板 讓你一次吃個夠!!! 每條魚版的魚漿比例高達60%，入口鮮美，魚香飄滿嘴!! 九種口味讓各位一飽口福: 青陽辣椒魚板:陽辣椒切碎後加入魚板，讓青陽辣椒獨有的辣香引出魚板鮮味，獨特辣感值得一試。 包心年糕魚板:韓國街頭最常見的小吃：年糕與魚板，兩者加在一起，也是釜山地區代表性的小吃。 海鮮魚板條:添加魷魚與多種魚肉，嚐到滿滿海鮮味 香菇魚板條:添加新鮮香菇使魚板的香氣更濃郁 蔬菜魚板片:加入洋蔥、紅蘿蔔等各種蔬菜 傳統魚板片: 魚漿比例高達60% 魷魚魚板樹:韓國國產魷魚製成魚板片，享受新鮮海味 三角冬粉魚板片:三角形狀 冬粉與魚漿的創新結合 蟹肉風味魚板:採新鮮蟹肉混和製作 韓國特色小吃 怎麼吃都好吃 可以像傳統一樣帶個辣炒年糕醬 回家拌炒著吃，超對味!! 也可以水煮熟透後，放上烤肉架刷醬吃超級讚!! 或者加入高湯熬煮暖心關東煮也很誘人 想怎麼吃就怎麼吃料理性 流行性十足的創意魚板就在這喔!!'
post2='*酥炸三節翅*酥炸三節翅(預炸)20入（1300g/包）團購價＋1＝160元最近肉品不知怎麼搞的漲價漲的亂七八~~~'
sample='A+2 C+3'



# def get_price(post):
#     pos=post.find('團購價')
    
#     price_text=''
#     token=[]
#     end_token=[]
#     mid_token=[]
#     price_dict={}
#     for i in post[pos+3:]:
#         if i!='!':
#             price_text+=i
#         if i=='!':
#             break
    
#     for i in range(len(price_text)):
#         if price_text[i]=='+' or price_text[i]=='＋':
#             token.append(i)
#         if price_text[i]=='元':
#             end_token.append(i)
#         if price_text[i]=='＝' or price_text[i]=='=':
#             mid_token.append(i)
            
#     for i in range(len(token)):
#         price_dict[price_text[token[i]+1]]=price_text[mid_token[i]+1:end_token[i]]
        
#     return(price_dict)
        




def get_product_dict(post):
    start_token=[]
    end_token=[]
    p_dict={}

    for i in range(len(post)):
        if post[i]=='.':
            start_token.append(i)
        elif post[i]=='~':
            end_token.append(i)
            
    
            
    for j in range(len(start_token)):
        tmp=''
        for k in range(len(post[start_token[j]+1:end_token[j]])):
            tmp+=post[start_token[j]+k+1]
        p_dict[post[start_token[j]-1]]=tmp
    

    return(p_dict)

    
            
        
    

def get_quantity(comment,token_lst):
    comment=comment+' '
    quantity_lst=[] 
    if len(token_lst)==0:
        return 0  
    for i in range(len(token_lst)):
        result=''      
        for char in comment[token_lst[i]+1:]:     
            if char.isdigit():            
                result+=char
            else:              
                quantity_lst.append(result)              
                break
    return quantity_lst
    

def get_product_info(comment,post_type,post):
    token=[]
    product_dict=get_product_dict(post)
    token_num=[]
    product_lst=[]
    product_output=''
    q_lst=[]
    for i in range(len(comment)):
        if comment[i]=='+':
#                確認有幾個+和+號的位置
            token.append(i)
        if comment[i].isnumeric()==True:
            token_num.append(i)
            
    if len(token)>0:
    
        for k in range(len(token)):
    #        看有幾個+就送幾個產品
            product_lst.append(comment[token[k]-1])    
            
    q_lst=get_quantity(comment,token)
    
    
    
    for index in range(len(product_lst)):
        if product_lst[index]==0:
            product_lst[index]='A'
    
    print(product_lst)
    if post_type==1:
        if len(product_lst)==0:
            return comment

        for n in range(len(q_lst)):

            product_output+='A:'+q_lst[n]
    
    if post_type!=1:
        
        if len(product_lst)==0:
            return comment
        
        for n in range(len(product_lst)):

            product_output+=product_dict[product_lst[n]]+':'+q_lst[n]+','


    
    return(product_output)
    
 
# print(get_product_info(sample,1,post2))