# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1 - (1**n - num)/(n * 1**(n-1))
    i = 1
    while i < t:
        x = x - (x**n - num)/(n * x**(n-1))
        i += 1
    return round(x, 3)

def nroot_complex(n,t,num):
    if num >= 0:
        return nroot(n,t,num)
    elif num <= 0:
        if n%2 == 0:
            