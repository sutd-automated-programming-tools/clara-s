# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x0 = 1
    counter = 0
    while counter <= i:
        f1 = x0**n-num
        f2 = n*x0**(n-1)
        x0 -= f1/f2 
        counter += 1
    return round(x0,3)

def nroot_complex(n,i,num):
    if n%2 == 0:
        output = nroot(n,i,-num)
        return output*1j
    else:
        return (nroot(n,i,num))