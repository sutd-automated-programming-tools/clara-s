# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    newnum = num
    for i in range(t):
        newnum = newnum - (newnum - num)/(n*newnum**n-1)
        n -= 1
    return newnum

def nroot_complex(n,t,num):
    pass