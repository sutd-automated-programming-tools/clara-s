#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:18:45 2018

@author: WuTong
"""

f = open("mrt_line_short.txt", "r")

def getMRT(f):
    lines = f.readlines()
    result = {}
    for line in lines:
        line = line.strip('=').split('\n')
        result[line[0]] = line[1:]
    return result
print(getMRT(f))
