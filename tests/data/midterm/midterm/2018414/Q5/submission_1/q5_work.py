# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for j in range(i):
        df = x**n - num
        dff = 2*x
        x = x - (df/dff)
    return round(x,3)

def nroot_complex(n,i,num):
    c = 1j
    if num <0: 
        if n%2 == 0:
            imag = nroot(n,i,-num)
            x = imag*c
        else:
            mag = nroot(n,i,-num)
            x = -mag
    else:
        x = nroot(n,i,num)
    return x