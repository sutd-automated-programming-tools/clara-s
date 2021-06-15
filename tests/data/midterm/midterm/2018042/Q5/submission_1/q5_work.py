# MID-TERM EXAM: QUESTION 5
import numpy as np
def nroot(n,t,num):
    x=1
    for i in range(t):
        f_x=x**n - num
        f__x=n*x**(n-1)
        x=x- f_x / f__x
    return round(x,3)
        

def nroot_complex(n,t,num):
    if n%2==0:
        x= int((nroot(n,t,-num)))* np.imag(1)
    else:
        x= round(nroot(n,t,-num),2)*(-1)
    return x
            
            
    
    