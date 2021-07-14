# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    def f(x):
        return x**n - num
    def f_(x):
        return n*x**(n-1)
    for k in range(t):
        x = x - f(x)/f_(x)
    return round(x,3)

def nroot_complex(n,t,num):
    if num > 0:
        return nroot(n,t,num)

    if num < 0:
        res = nroot(n,t,-num)
        if n%2 == 0:
            k = True
        else:
            k = False

    if num >0:
        return res
    if k:
        return res*1j
    else:
        return -res