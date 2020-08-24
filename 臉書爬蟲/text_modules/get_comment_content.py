#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:40 2020

@author: cheer
"""

comment='某某某A+1,B2,C3,取貨'

def get_comment_content(comment,post_type):
    plus_token=[]
    for i in range(len(comment)):
        if comment[i]=='+':
            plus_token.append(i)
            
    if len(plus_token)==0:
        return(comment)
        
    elif post_type==0:
        return(comment)
    elif post_type==1 :
        return comment[plus_token[0]:]
    elif post_type==2:
        return comment[plus_token[0]-1:]
            
    


