# MID-TERM EXAM: QUESTION 5

import cmath

def nroot(n,t,num):
    x_0 = 1
    for a in range(t):
        f_x = x_0**n - num
        f_der_x = n*x_0**(n-1)
        x_0 = x_0 - (f_x)/(f_der_x)
    return round(x_0,3)

def nroot_complex(n,t,num):
    if n % 2 == 0:
        num = -1*num
        output = nroot(n,t,num)
        z = complex(0,output)
    
    if n % 2 != 0:
        num = -1*num
        output = nroot(n,t,num)
        z = -1*round(output,3)
        
  
    return z