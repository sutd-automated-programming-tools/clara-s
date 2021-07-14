#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:06:10 2018

@author: WuTong
"""

def decompose(pence):
    d=list(range(pence))
    n=0
    if pence < 2 < 5:
        n=pence
    if pence  >5:
        for i in d:
            for j in d:
                if i+ 2j == pence:
                    n+=1
    return n

print(decompose(6))
        
        
    