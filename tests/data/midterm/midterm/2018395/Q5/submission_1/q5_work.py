# MID-TERM EXAM: QUESTION 5

import math
def nroot(n,t,num):
    
    a = 0
    x = 1
    while a<t:
    
        y = x**n - num
        dy = n*x**(n-1)
        x = x -(y/dy)
     
        a += 1
    
    return x
        
    

def nroot_complex(n,t,num):
    
    y = nroot(n,t, num)
    
    return y