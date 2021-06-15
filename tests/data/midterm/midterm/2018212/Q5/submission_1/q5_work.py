# MID-TERM EXAM: QUESTION 5
import copy
def nroot(n,t,num):
    x=copy.deepcopy(num)
    while t>=0:
        f=x**t-num
        f_prime=t*x**(t-1)
        x-=f/f_prime
        t-=1
    return round(x,3)

def nroot_complex(n,t,num):
    if num>=0:
        return nroot(n,t,num)
    elif num<0 and n%2==0:
        return complex(0,(-1)*nroot(n,t,num))
    elif num<0 and n%2!=0:
        return (-1)*nroot(n,t,num)
        