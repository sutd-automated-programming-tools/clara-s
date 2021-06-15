# Q5: Newton Raphson
def nroot(n, i, num):
    xn = 1
    count = 0
    while count < i:
        fx = xn ** n - num
        fpx = n * xn ** (n - 1)
        xn -= (fx / fpx)
        # print(xn)
        count += 1
    return round(xn, 3)


def nroot_complex(n, i, cnum):
    real_r = nroot(n, i, -cnum)
    if n % 2 == 0:
        return real_r * 1j
    else:
        return -real_r