# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:49:06 2018

@author: xinya
"""

#6
a)
def read_stations(f):
    d = {}
    lst=[]
    lst1 = []
    for line in f:
        output = line.strip()
        lst.append(output)
    for i in lst:
        output = i.split(", ")
        lst1.append(output)
    for i in lst1:
        d[i[0]]=i[1:]
    return d   
    
f = fd =open("mrt.txt","r")
b)
def get_stationline(mrt):
    
c)
def get_interchange(stationline):
    
d)
def find_path(f, start, end):