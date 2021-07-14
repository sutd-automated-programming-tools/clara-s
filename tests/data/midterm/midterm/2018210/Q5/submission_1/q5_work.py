def NR(x, n, num):
    f = (x ** n) - num
    f_prime = n * (x ** (n - 1))
    term = f / f_prime
    return term


def nroot(n, i, num):
    x = 1
    output = 1
    while x < i:
        output = output - NR(x, n, num)
        x += 1
    return output


def nroot_complex(n, i, num):
    if n < 0 and n%2 == 0:
        return nroot(n,i,num)*1j
    elif n < 0 and n%2!=0:
        return nroot(n,i,num)
    else:
        return nroot(n,i,num)
    pass