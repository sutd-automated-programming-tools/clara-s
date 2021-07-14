# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    for j in range(2,i):
        x = x - (x**2 -num)/(2*x)
    return round(x,3)

def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    else:
        if n%2 == 0:
            return int(nroot(n,i,-num))*1j
        else:
            return float(int(nroot(n,i,-num)))*-1