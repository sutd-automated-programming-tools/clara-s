# MID-TERM EXAM: QUESTION 5
import numpy as n
def nroot(n,t,num):
    x = num **(1/n)
    
    return x 

def nroot_complex(n,t,num):
    if num > 0:
        return (nroot(n,t,num))
    elif num < 0 and num%2 == 0:
        return n.imag(nroot(n,t,num))
    elif num < 0 and num%2 == 1:
        return -n.real(nroot(n,t,num))