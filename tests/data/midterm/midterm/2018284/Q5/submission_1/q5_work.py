# MID-TERM EXAM: QUESTION 5

def f(x,n,num) :
    return x**n-num
def df(x,n) :
    return n*x**(n-1)

def nroot(n,t,num):
    x = 1
    for j in range(t):
        x = x-f(x,n,num)/df(x,n)
    return round(x,3)

def nroot_complex(n,t,num):
    if num<0 and n%2== 0:
        return nroot(n,t,-1*num)*1j
    elif num<0 and n%2== 1:
        return nroot(n,t,-1*num)*-1
    else :
        return nroot(n,t,num)
