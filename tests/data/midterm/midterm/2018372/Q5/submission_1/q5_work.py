def nroot(n, i, num):
    c = 0
    while c <= i:
        x = (num)**(1/n)
        x2 = num
        fx = x2 - num
        fx1 = 2*x
        xi = x - (fx/fx1)
        x = xi
        c += 1
    if num > 0:
        return round(xi,3)
    else:
        y = round(xi.imag)
        return ("{}j".format(y))
        

def nroot_complex(n,i,num):
    xi = nroot(n, i, num)
    if num > 0:
        return round(xi,3)
    else:
        y = xi
        return y