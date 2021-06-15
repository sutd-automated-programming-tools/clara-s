# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for k in range(i):
        fx = (x ** n) - num
        fxp= n * x ** (n - 1)
        x = x - (fx / fxp)
    return round(x , 3)

def nroot_complex(n, i, num):
    nroot(n, i, num)
    return x