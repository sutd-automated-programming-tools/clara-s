# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for sth in range(i):
        x = x-(x**2-num)/(2*x)
    return round(x,3)

def nroot_complex(n,i,num):
    x = 1
    if num >=0:
        return nroot(n,i,num)
    elif num <0 and n%2==0:
        for sth in range(i):
            x = x-(x**2-num)/(2*x)
        x = round(x,3)
        x = x*1j
        return x
    elif num <0 and n%2!=0:
        for sth in range(i):
            x = x-(x-num**0.5)/(2*x)
            x = (x.imag**2+x.real**2)**0.5
        return x