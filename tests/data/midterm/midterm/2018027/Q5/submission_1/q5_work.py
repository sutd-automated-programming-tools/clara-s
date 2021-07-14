# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if t == 1:
        return num**(1/n)
    else:
        res = nroot(n,t-1,num)-(nroot(n,t-1,num)**n-num)/n*nroot(n,t-1,num)
        return round(res,3)

def nroot_complex(n,t,num):
    if n % 2 == 1:
        return -nroot(n,t,-num)
    elif n % 2 == 0:
        return nroot(n,t,-num)*1j