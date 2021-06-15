# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(n+1):
        numer = (x ** n) - num
        denom = (n * x)
        x = x - (numer/denom)
    return round(x,3)
    pass

def nroot_complex(n,t,num):
    x = nroot(n,t,num)
    if n % 2 == 0:
        return x*1j
    else:
        return x.real
    pass