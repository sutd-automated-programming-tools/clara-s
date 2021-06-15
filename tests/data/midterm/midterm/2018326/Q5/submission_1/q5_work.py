def nroot(n,i,num):
    x=1
    for k in range(i+1):
        x=x-(x**n-num)/(n*x**n-1)
    return round (x,3)

def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,num)
    else:
        if n%2==0:
            return str(int(nroot(n,i,-num)))+"j"
        else:
            return -nroot(n,i,-num)