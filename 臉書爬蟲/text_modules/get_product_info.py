#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:16:14 2020

@author: cheer
"""
sample='黃晉豪 幹你老師'



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
    

def get_product_info(comment,post_type):
    token=[]
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
    
    
    if post_type==1:
        if len(product_lst)==0:
            return comment

        for n in range(len(q_lst)):

            product_output+='A:'+q_lst[n]
    
    if post_type!=1:
        
        if len(product_lst)==0:
            return comment
        
        for n in range(len(product_lst)):

            product_output+=product_lst[n]+':'+q_lst[n]+' '
#    
#    for n in range(len(product_lst)):
#        product_output+=product_lst[n]+':'+q_lst[n]+' '
#        print(product_output)


    
    return(product_output)
    
 
print(get_product_info(sample,2))