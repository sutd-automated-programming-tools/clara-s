# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    nrt=num**(1/n)
    nrt=round(nrt,3)
    return nrt

def nroot_complex(n,t,num):
    if num<=0:
        return (nroot(n,t,num))
    else:
        pass