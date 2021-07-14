# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    def f(x):
        return x**n - num
    def fp(x):
        return n*x**(n-1)
    x = num
    for j in range(i+1):
        x = x - f(x)/fp(x)
    return round(x,3)

def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,num)
    if n%2==0:
        return nroot(n,i,-num)*1j
    return -1 * nroot(n,i,-num)