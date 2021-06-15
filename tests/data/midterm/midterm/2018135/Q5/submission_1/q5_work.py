# MID-TERM EXAM: QUESTION 5
from math import *
import numpy as np
def nroot(n,i,num):
    x = 1
    if num != 0 and n > 0:
        for m in range(1,i+1):
            x -= (x**n-num)/(n*x**(n-1))
            
    return round(x,3)
        
def nroot_complex(n,i,num):
    ans1 = nroot(n,i,num)
    if num < 0:
        if n%2 != 0:
            ans = nroot(-n,i,num)
        if n%2 == 0:
            const = ans1/np.imag(sqrt(-1))
            return const*{}.format('j')
        
    return ans
            