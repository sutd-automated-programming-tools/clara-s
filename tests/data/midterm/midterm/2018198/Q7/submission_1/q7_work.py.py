# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:04:51 2018

@author: Jia Yi
"""

def decompose(pence):
    pence = int(input("Enter number of pence: "))
    
    p1 = pence
    
    if pence%2 == 0:
        p2 = 2
    else:
        p2 = 0
    
    
    if pence%5 == 0:
        p5 = pence
    else:
        p5 = 0
        
    p5 = p5 * 3
        
    if pence%10 == 0:
        p10 = pence//10
    else:
        p10 = 0
    
    p10 = p10 * 9
        
    if pence%20 == 0:
        p20 = pence//20
    else:
        p20 = 0
    
    p20 = p20 
        
    if pence%50 == 0:
        p50 = pence//50
    else:
        p50 = 0
        
    if pence%100 == 0:
        p100 = pence//100
    else:
        p100 = 0
    
    if pence%200 == 0:
        p200 = pence//200
    else:
        p200 = 0
        
    #2p = 2 * 1p
    number = p1 + p2 + p5 + p10 + p20 + p50 + p100+ p200
    return number

print(decompose(1))
print(decompose(5))
print(decompose(7))