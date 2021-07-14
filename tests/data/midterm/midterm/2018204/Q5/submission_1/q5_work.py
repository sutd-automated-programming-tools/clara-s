# MID-TERM EXAM: QUESTION 5

import math
import numpy as np
def nroot(n,t,num):
    p = n
    x = 1
    for i in range(t):
        x = x - (x**p - num)/(p*x**(p-1))
    return round(x, 3)      

def nroot_complex(n,t,num):
    if num < 0 and n%2 == 0:
        return nroot(n, t, -num) #i can't insert j for some reason
        
    elif num < 0 and n%2 != 0:
        return nroot(n, t, -num)*-1