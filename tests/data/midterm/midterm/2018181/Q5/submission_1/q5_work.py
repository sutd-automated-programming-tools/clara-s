# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    for h in range(i):
        x=x-(x**n-num)/(n*x**(n-1))
    return round(x,3)
def nroot_complex(n,i,num):
    if n%2==1:
        return -nroot(n,i,-num)
    if n%2==0:
        return nroot(n,i,-num)*1j