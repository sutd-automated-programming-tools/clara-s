#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:39:10 2018

@author: kundandalmia
"""

def decompose(pence):
    
    
    def step(given, val):
        if given < val:
            return 0
        elif given == val:
            return 1
        else:
            return step(given, val*2) + step(given-val, val)
    return step(pence, 1)


