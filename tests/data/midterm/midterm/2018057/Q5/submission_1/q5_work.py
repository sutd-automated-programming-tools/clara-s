# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    
#    x = num**(1/n)
    xit = num**(1/n)
    for it in range(1,i):
        xit -= ((xit**n)-num)/(n*xit**(n-1))
    return round(xit,3)

def nroot_complex(n,i,num):
    xit = num**(1/n)
    for it in range(1,i):
        xit -= ((xit**n)-num)/(n*xit**(n-1))
    if num%2 == 1:
        return xit
    elif num%2 == 0:
        return xit