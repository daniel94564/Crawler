#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:40 2020

@author: cheer
"""

comment='某某某A+1,B2,C3,取貨'

def comment_content(comment):
    plus_token=[]
    for i in range(len(comment)):
        if comment[i]=='+':
            plus_token.append(i)
            
    if len(plus_token)==0:
        return(comment)
    else :
        return comment[plus_token[0]-1:]
            
    

print(comment_content(comment))

