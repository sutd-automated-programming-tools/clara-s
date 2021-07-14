# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    nroot(0) = 1
    fx = x**(n-1) - num
    deriv = n*(x)**(n-2)
    return nroot(n-1) - fx/deriv

def nroot_complex(n,t,num):
    pass