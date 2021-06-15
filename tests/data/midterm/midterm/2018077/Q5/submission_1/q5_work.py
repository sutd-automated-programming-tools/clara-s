# MID-TERM EXAM: QUESTION 5
from decimal import *    
import math
import cmath


def nroot(n,t,num):
    root=(num)**(1/n)
    return root

def nroot_complex(n,t,num):
    if num>=0:
        return nroot(n,t,num)
    elif num<0 and n%2==0:
        return 1j*(nroot(n,t,num))
    elif num<0 and n%2!=0:
        return (abs(nroot(n,t,num))*-1)