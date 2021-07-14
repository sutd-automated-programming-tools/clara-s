# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if n==1:
        x = num
    if n>1:
        x = nroot(n,t,num)-fx/fdx
        fx = x**n - num
        fdx = n*x**(n-1)
    return x

def nroot_complex(n,t,num):
    pass