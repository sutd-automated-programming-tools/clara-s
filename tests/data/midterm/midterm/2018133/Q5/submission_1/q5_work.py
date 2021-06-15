# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    nroot = 1
    nroot**n = num
    fx = nroot**n-num
    dfx = n*nroot**(n-1)
    for i in range(t):
        nroot = nroot - fx/dfx
    return nroot
    

def nroot_complex(n,t,num):
    pass