# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    newnum = 1
    for j in range(i):
        fx = (newnum)**(1/n)
        fprimex = n*num
        newnum = newnum - (fx/fprimex)
    return newnum

def nroot_complex(n,t,num):
    pass