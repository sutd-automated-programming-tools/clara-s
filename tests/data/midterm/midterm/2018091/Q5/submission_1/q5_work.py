# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for k in range(i):
        x -= (x**n - num)/(n*x**(n-1))
    return round(x, 3)

def nroot_complex(n, i, num):
    if num > 0:
        return nroot(n, i, num)
    elif n%2:
        return nroot(n, i, num)
    else:
        return 1j*nroot(n, i, -num)