#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:43:40 2020

@author: cheer
"""



def get_post_content(post):
    start_end_token=[]
    post_type=0
    for i in range(len(post)):
        if post[i]=='*':
            start_end_token.append(i)
            post_type=1
        if post[i]=='^':
            start_end_token.append(i)
            post_type=2
    
    return(post[start_end_token[0]+1:start_end_token[1]],post_type)
    

