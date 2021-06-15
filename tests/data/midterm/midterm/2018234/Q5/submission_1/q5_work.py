# MID-TERM EXAM: QUESTION 5

import math 
def nroot(n,t,num):
    #determine root of non-negative num
    x = n** math.sqrt (num)          #x is in nth root of num 
    x = 1
    fx = x**2 - num
    f_x = 2 * x
    x_ith = x - fx/f_x
    return float(x_ith)
    print (x_ith)
    
def nroot_complex(n,t,num):
#    determine root of negative num 
        #    calls nroot to do NR approx
    
    return nroot_complex

