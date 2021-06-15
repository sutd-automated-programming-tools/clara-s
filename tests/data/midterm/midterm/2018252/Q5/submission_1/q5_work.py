# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    count=0
    x=1
    while count <i:
        x=x-(x**n-num)/(num*(x**(num-1)))
        count += 1
    x=round(x,3)
    return x

def nroot_complex(n,i,num):
    if n%2 != 0:
        out=nroot(n,i,-num)
        out=-out
        return out
    else:
        out=nroot(n,i,-num)
        out=out*1j
        return out