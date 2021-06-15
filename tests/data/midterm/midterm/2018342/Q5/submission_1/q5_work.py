# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = num ** (1/n)
    for j in range(i):
        x = x - (x ** 2 - num) / (2 * x)
    return x

def nroot_complex(n, i, num):
    if num >= 0:
        return nroot(n, i, num)
    else:
        if num % 2 == 0:
            return  str(nroot(n, i, num))
        else:
            return nroot(n, i, num)