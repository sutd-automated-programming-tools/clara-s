# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    if num < 0:
        x = (-num) ** (1/n)
    else:
        x = (num) ** (1/n)
    return round(x, 3)

def nroot_complex(n, i, num):
    x = nroot(n, i, num)
    if n % 2 == 0:
        im = 1j
    else:
        im = -1
    return x*im