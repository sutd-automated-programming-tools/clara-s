# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    g = x ** n 
    f = g - num
    f_prime = n * x ** (n-1)
    for i in range(t):
        x = x - f / f_prime
        g = x ** n
        f = g - num
        f_prime = n * x ** (n-1)
    return round(x, 3)
        

def nroot_complex(n,t,num):
    if num > 0:
        return nroot(n, t, num)
    elif num < 0:
        num = num / -1
    x = 1
    g = x ** n 
    f = g - num 
    f_prime = n * x ** (n-1)
    for i in range(t):
        x = x - f / f_prime
        g = x ** n
        f = g - num
        f_prime = n * x ** (n-1)
    if n % 2 == 0:
        x = round(x)
        return (x * 1j)
    return round(-x, 3)