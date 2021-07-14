# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x=num
    a=1
    while a<=t+1:
        y=x**n-num
        z=n*(x**(n-1))
        x=x-y/z
        a+=1
    return round(x,3)

def nroot_complex(n,t,num):
    if n%2==0:
        ans=nroot(n,t,num)*1j
    else:
        ans=nroot(n,t,num)
    return ans