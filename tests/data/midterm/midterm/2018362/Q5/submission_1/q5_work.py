#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:30:46 2018

@author: rachelsongg
"""

#B Q5

# function to differentiate polynomial
def diff(p):
    if 0 in p:                  #delete constants in polynomial
        del p[0]
    dp = {}
    diffno = 0
    
    for (x, y) in p.items():
        xx = x - 1
        yy = x*y
        dp[xx] = yy

# make dictionary of differentiated polynomials into a string    
    for coeff in dp:
        diffno += coeff.getvalue()**coeff.getkey()
        return str(diffno)


def nroot(n, i, num):
    p = {n: num}
    
# p = {n: num}
# use ith iteration for the first time: x(1) = x(0) - (x**n - num)/(diff(p))
#repeat iteration for i times: x(2) = x(1) - (diff(p))/diff(p)
    

    
