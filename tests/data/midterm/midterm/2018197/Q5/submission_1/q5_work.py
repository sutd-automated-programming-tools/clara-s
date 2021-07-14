# MID-TERM EXAM: QUESTION 5
import math
def nroot(n,i,num):
    #x2=num
    x=1
    for i in range(i):
        fx=x**2-num
        dfx=2*x
        x=x-fx/dfx
    return round(x,3)
    pass

def nroot_complex(n,i,num):
    if num>0:
        return nroot(n,i,num)
    else:
        num=num*-1
        a=nroot(n,i,num)
        if n%2==0:
            return a*1j
        else:
            return -1*a
    pass