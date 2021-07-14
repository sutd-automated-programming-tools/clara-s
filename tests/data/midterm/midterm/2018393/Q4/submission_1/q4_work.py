#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:30:27 2018

@author: WuTong
"""

def determinant(matrix):
    a=0
    for i in matrix:
        a+=len(i)
    if not a%2==0:
        return None
    else:
        if a==4:
            for i in matrix:
                s=i[0]
                    


            sum=s
        return sum
                    
    
print(determinant([[-5,-4],[-2,-3]]))
        