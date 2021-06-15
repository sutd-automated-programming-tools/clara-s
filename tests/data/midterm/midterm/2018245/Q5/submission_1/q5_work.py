def nroot(n, i, num):
    x = 1
    while i>0:
        x = x - (x**n - num)/(n*x)
        i -= 1
    return round(x,3)

def nroot_complex(n,i,num):
    if (n%2 == 0) and (num<0):
        num = -num
        return nroot(n, i, num) * 1j
    elif (n%2==1) and (num<0):
        return nroot(n, i, num)
    else:
        return nroot(n, i, num)