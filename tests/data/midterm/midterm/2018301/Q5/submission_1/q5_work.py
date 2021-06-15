# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    index=0
    while index<(i):
        fx=(x**n)-num
        fpx=n*(x**(n-1))
        ans=x-(fx/fpx)
        x=ans
        index+=1
    return round(x,3)

def nroot_complex(n,i,num):
    if num>0:
        ans=nroot(n,i,num)
    if num<0 and n%2==0:
        new=-num
        ans=nroot(n,i,new)*1j
    if num<0 and n%2!=0:
        new=-num
        ans=(-1)*(nroot(n,i,new))
    return ans