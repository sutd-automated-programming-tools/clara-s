# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    pass

def nroot_complex(n,t,num):
    pass
def nroot(n, i, num):
    x0 = 1
    for iteration in range(i):
        y = x0 ** n - num
        yder = n * x0 ** (n-1)
        x0 = x0 - y / yder
    return round(x0, 3)


def nroot_complex(n, i, num):
    if num >= 0:
        return nroot(n, i, num)
    else:
        
        if n % 2 == 0:
            
            return nroot(n, i, -num) * 1j
        else:
            return -nroot(n, i, -num)