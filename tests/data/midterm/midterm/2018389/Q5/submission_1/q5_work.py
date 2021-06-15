# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(1, t+1):
        x = x - (x**n - num)/(n*(x**(n-1)))
    return round(x,3)

def nroot_complex(n,t,num):
    k = 1j
    if num >= 0:
        return round(nroot(n,t,num), 3)
    elif num < 0 and n%2 == 0:
        return round(nroot(n,t,-num), 3)*k
    elif num < 0 and n%2 != 0:
        return round((-(nroot(n,t,-num))),3)