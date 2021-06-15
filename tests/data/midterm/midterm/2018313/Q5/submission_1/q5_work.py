# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    if n == 1:
        return num
    for y in range(i):
        x = x - (x**n - num)/(n*(x**(n-1)))
    return round(x,3)

def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0 and n % 2 == 0:
        result = 1j*(nroot(n,i,-num))
        return result
    elif num < 0 and n% 2 != 0:
        result = -nroot(n,i,-num)
        return result