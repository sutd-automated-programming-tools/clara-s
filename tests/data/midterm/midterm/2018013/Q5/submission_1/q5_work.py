# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x0=1
    for i in range(t):
        x0=x0-(x0**n-num)/(n*x0**(n-1))
        x0=round(x0,3)
    return x0
    

def nroot_complex(n,t,num):
    if num>0:
        return nroot(n,t,num)
    elif num<0 and n%2==0:
        return (nroot(n,t,-num)*1j)
    else:
        return(-nroot(n,t,-num))