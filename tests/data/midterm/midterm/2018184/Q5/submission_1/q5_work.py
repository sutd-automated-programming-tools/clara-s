# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if t == 1:
        return num
    elif t>1:
        x = num**(1/n)
        return nroot(t-1)
    

def nroot_complex(n,t,num):
    pass