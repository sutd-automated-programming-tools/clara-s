# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    for j in range(i):
        f=x**n-num
        derivf=n*x**(n-1)
        x=x-f/derivf
    x=round(x,3)
    return x

def nroot_complex(n,i,num):
    if n%2==0:
        ans=complex(0,nroot(n,i,-num))
    elif n%2!=0:
        ans=nroot(n,i,num)
    return ans