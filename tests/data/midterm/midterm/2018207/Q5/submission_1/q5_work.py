# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = n
    for i in range(1,i):
        fx = x**n - num
        fpx = n*x**(n-1)
        x -= fx/fpx
    return round(x,3)

def nroot_complex(n,i,num):
    if num >= 0:
        return nroot(n,i,num)
    
    else:
        if n  %2 == 0:
            return nroot(n,i,-num)*1j

        else:
            return -1*nroot(n,i,-num)