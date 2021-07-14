# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = num ** (1/n)
    return round(x, 3)


def nroot_complex(n, i, num):
    num = abs(num)
    x = nroot(n, i, num)
    if n % 2 != 0:
        x = 0 - x
    else:
        x = 1j * x
    return x