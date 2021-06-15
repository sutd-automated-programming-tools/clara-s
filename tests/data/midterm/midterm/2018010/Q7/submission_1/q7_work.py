# MID-TERM EXAM: QUESTION 7

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:23:24 2018

@author: Benjamin
"""

def decompose(pence):
    ls = [1,2,5,10,20,50,100,200]
    count = 0
    if pence == 1:
        return count
    else:
        if pence - 200 > 0:
                   
            return decompose(pence -200)
            count+=1
        elif pence - 100 > 0:
                   
            return decompose(pence -100)
            count+=1
        elif pence - 50 > 0:
                   
            return decompose(pence - 50)
            count+=1
        elif pence - 20 > 0:
                   
            return decompose(pence -20)
            count+=1
        elif pence - 10 > 0:
                   
            return decompose(pence - 10)
            count+=1
        elif pence - 5 > 0:
                   
            return decompose(pence - 5)
            count+=1
        elif pence - 2 > 0:
                   
            return decompose(pence - 2)
            count+=1
        elif pence - 1 > 0:
                   
            return decompose(pence - 1)
            count+=1
        