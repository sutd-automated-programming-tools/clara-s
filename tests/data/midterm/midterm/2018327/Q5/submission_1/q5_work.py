# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x=1
    for j in range(t):
        x-=(x**n-num)/(n*x**(n-1))
    return round(x,3)
    pass
def nroot_complex(n,t,m):
    if m>=0:
        return nroot(n,t,m)
    elif n%2==0:
        return nroot(n,t,-1*m)*1j
    else:
        return nroot(n,t,-1*m)*-1
    pass