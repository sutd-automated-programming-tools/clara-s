def nroot(n , i , num):
    if i == 1:
        x = 1
    else:
        x = nroot(n, i-1, num)
    fx = x**n - num
    fpx = n*(x**(n-1))
    return(round(x - (fx/fpx),3))

def nroot_complex(n, i, num):
    num = complex(num)
    if i == 1:
        x = 1
    else:
        x = nroot_complex(n, i-1, num)
    fx = x**n - num
    fpx = n*(x**(n-1))
    return(round(x - (fx/fpx),3))