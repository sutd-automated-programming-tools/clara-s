# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    m=1
    x=1
    while m<=t:
        x=x-(x**n-num)/(n*x**(n-1))
        m+=1
    return round(x,3)
def nroot_complex(n,t,num):
    if num>=0:
        return nroot(n,t,num)
    elif num<=0 and n%2==0:
        rt=nroot(n,t,-num)*1j
        return rt
    elif num<=0 and n%2==1:
        return nroot(n,t,num)