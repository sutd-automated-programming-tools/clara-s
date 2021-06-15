# MID-TERM EXAM: QUESTION 5
def f(x, num):
    f = (x**2)-num
    return f

def f_(x, num):
    f = 2*x
    return f

def nroot(n, i, num):
    x = 1
    if i == 1:
        x = 1
    else:
        x = float(nroot(n, (i-1), num) - ((f(nroot(n, (i-1), num), num)) / f_(nroot(n, (i-1), num), num)))
        x = round(x, 3)
    return x

def nroot_complex(n, i, num):
    if num<0:
        if n%2 == 0:
            g = 0
            x = nroot(n, i, -num)
            g = complex(0, x)
            return g
        elif n%2 == 1:
            x = x = nroot(n, i, -num)
        return -int(x)