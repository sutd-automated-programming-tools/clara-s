# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:48:33 2018

@author: xinya
"""

#5    
def nroot(n, i, num):

def nroot_complex(n, i, num):

if num 

    
    
def absolute(cn):
    x=cn.real
    y=cn.imag
    absolute_cn=sqrt(x**2+y**2)
    absolute_cn=float(absolute_cn)
    return absolute_cn


def distance (d,s):
    stations = s.split(", ")
    lst = []
    #get line of the 2 stations
    for k, v in d.items():
        for i in stations:
            if i in v:
                lst.append(k)
    if len(stations)<2:
        return -1
    if lst[0]==lst[1]:
        distance = d[lst[0]].index(stations[1])-d[lst[0]].index(stations[0])
        return distance
    if lst[0]!=lst[1]:
        return -1
    

d = getMRT(f)
s = "Pasir Ris"
print distance(d, s)