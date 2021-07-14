# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    f = n**2 - num
    fprime = 2*n
    i -= 1
    return nroot(n,i,num) - (f / fprime)

def nroot_complex(n,t,num):
    pass