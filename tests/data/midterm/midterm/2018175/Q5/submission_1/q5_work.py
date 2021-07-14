# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    def f(x, n, num):
        f = x ** n - num
        return f
    
    def f_prime(x, n, num):
        f_prime = n * (x ** (n-1))
        return f_prime

    
    for k in range(t):    
        x = x  - (f(x, n, num) / f_prime(x, n, num))

def nroot_complex(n,t,num):
    pass