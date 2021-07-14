# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = abs(num)
    for a in range(t):
        x += - f(n,x,num)/df(n,x,num)
    return round(x,3)


def nroot_complex(n,t,num):
    x = nroot(n,t,num)
    if n%2 != 0:
        return round(-x,1)
    else:
        return x*1j
    

def f(n,x,num):
    return x**n - abs(num)

def df(n,x,num):
    return (n)*x**(n-1)