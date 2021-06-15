# MID-TERM EXAM: QUESTION 5

def fox(n,x,num):
    fx = x**n - num
    return fx
def foxd(n,x):
    fxd = n*x**(n-1)
    return fxd
def nroot(n,i,num):
    xi = 1
    for i in range(200):
        xi = xi - fox(n,xi,num)/foxd(n,xi)
    return round(xi,3)

def nroot_complex(n,x,num):
    if num>0:
        return nroot(n,x,num)
    elif num<0 and n%2 == 0:
        return complex(0,nroot(n,x,-num))
    elif num<0 and n%2 != 0:
        return complex(-nroot(n,x,-num),0)
    else:
        return 0