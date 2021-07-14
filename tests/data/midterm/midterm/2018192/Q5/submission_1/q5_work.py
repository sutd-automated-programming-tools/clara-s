import math

def nroot(n, i, num):
    x = num**(1/n)
    for a in range(i):
        fx = x**n - num
        fpx = n*x**(n-1)
        
        x = x - fx/fpx
    return round(x,3)

def nroot_complex(n, i, num):
    if num <0:
        if n%2==0:              #n is even
            num = abs(num)
            root = nroot(n, i, num)
            return root*1j
        else:                   #n is odd
            num = abs(num)
            root = nroot(n, i, num)
            return root*(-1)
    else:
        return nroot(n, i, num)