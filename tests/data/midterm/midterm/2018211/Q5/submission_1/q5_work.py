# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(t):
        x -= ((x**n - num)/(n*(x**(n-1))))
    return round(x,3)

def nroot_complex(n,t,num):
    if num > 0 or num == 0:
        return nroot(n,t,num)
    if num < 0 and n%2 == 1:
        return -nroot(n,t,-num)
    else:
        return nroot(n,t,-num)*1j
        