#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:26:52 2020

@author: cheer
"""

location_list=['乖寶','科技園區','總部','陽光','品皇','瘋拍','珍Q','阿默','慈德','延平','大福']

def location(comment):
    flag=[]
    counter=0
    tmp=[]
    
    for i in range(len(location_list)):
        if location_list[i] in comment:
            flag.append(i)
            counter+=1
            
    if counter==1:
        return location_list[flag[0]]
    if counter>1:
        
        for i in range(counter):
            tmp.append(location_list[flag[i]])
        return tmp
    if counter==0:
        return "無取貨地點"
    
