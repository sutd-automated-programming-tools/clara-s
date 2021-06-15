# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if num<0:
        num=nroot_complex(n,t,num)
    x=1
    f=1**n-num
    fp=n*x
    for iterations in range(t):
        x=x-(f/fp)
        f=x**n-num
        fp=x*n
    x=(round(x,3))

    return x

def nroot_complex(n,t,num):
    c=num
    c=c**2
    c=c**0.5
    d=nroot_complex(n,t,c)
    if num<0:
        if n%2==0:
            #even
            d=-1*d
        else:
            d=-1*d
    
    return c
    