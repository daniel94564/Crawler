#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:20 2020

@author: cheer
"""




def get_comment_name(content,post_type):
    token=[]
    for i in range(len(content)):
        if content[i]=='+':
            token.append(i)
    if len(token)==0:
        return(content)
    elif '作者' in content:
        pos_author=content.rfind('作者')
        return(content[:pos_author])
    
    elif post_type==0:
        
        return(content)
        
    elif post_type==1:

        return(content[:token[0]])
    elif post_type==2:

        return(content[:token[0]-1])

            
        
