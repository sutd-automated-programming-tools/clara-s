# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
#    x=(num)**(1/n)
    x0=1
    x1=0
    for i in range(i):
        x1=x0-(x0**n-num)/(n*x0**(n-1))
        x0=x1
    return round(x1,3)

def nroot_complex(n,t,num):
    if num >=0:
        return nroot(n,t,num)
    elif n%2 == 0:
        return nroot(n,t,-num) *1j
    else:
        return -1*nroot(n,t,-num)