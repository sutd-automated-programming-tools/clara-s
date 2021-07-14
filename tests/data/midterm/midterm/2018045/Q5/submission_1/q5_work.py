import math

def nroot(n,i,num):
    x = 1
    for i in range(i):
        fx = x**n - num
        fpx = n*(x**(n-1))
        x = x - fx/fpx
    x = round(x,3)
    return x

def nroot_complex(n,i,num):
    if num>0:
        x = nroot(n,i,num)
    if num<0 and n%2==0:
        x = nroot(n,i,abs(num))
        x = complex(0,x)
    if num<0 and n%2==1:
        x = nroot(n,i,num)
        x = x.real
    return x