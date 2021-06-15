def nroot(n, i, num):
    return num**(1/n)

def nroot_complex(n, i, num):
    if num >= 0:
        return nroot(n, i, num)
    else:
        if n%2 == 0:
            return nroot(n, i, abs(num))*1j
        else:
            return nroot(n, i, abs(num))