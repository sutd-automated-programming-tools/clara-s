# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    f(x) = x**n - num
    df(x) = n*(x**(n-1))
    newx = x - f(x)/df(x)
    if num >= 0:
        return x

def nroot_complex(n,i,num):
    f(x) = x**n - num
    df(x) = n*(x**(n-1))
    newx = x - f(x)/df(x)
    if num >= 0:
        return nroot
    elif num <= 0:
        num%2=0
        return num 