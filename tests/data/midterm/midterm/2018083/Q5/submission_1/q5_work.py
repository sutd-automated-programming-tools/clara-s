# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if num <0:
        return None
    root=1/n
    x=num**root
    for i in range(t-1):
        x=x-(x**root)/(root*num**(root-1))
    return x
    

def nroot_complex(n,t,num):
    pass