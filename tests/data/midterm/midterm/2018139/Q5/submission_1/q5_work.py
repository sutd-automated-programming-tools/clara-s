# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    i = 0
    x_ite = num**(1/n)
    def yfunc(x_ite, num, n):
        return (x_ite**n - num)
    def yprimefunc(x_ite, n):
        return (n * x_ite**(n-1))
    while i < t:
        x_ite-= yfunc(x_ite, num, n) / yprimefunc(x_ite, n)
        n-= 1
        i+= 1
    return x_ite
        

def nroot_complex(n,t,num):
    pass