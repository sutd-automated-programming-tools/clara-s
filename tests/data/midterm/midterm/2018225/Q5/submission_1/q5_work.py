# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for j in range(0,i):
        fxi = (x**n) - num
        dfxi = n*(x**(n-1))
        xi = (x - (fxi/dfxi))
        x = xi
    return round(xi,3)
def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0 and n%2 == 0:
        return nroot(n,i,-num)*1j
    elif num < 0 and n%2 != 0:
        return nroot(n,i,num)