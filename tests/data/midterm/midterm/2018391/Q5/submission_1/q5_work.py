# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x**n=num
    f(x)=x**n-num
    f_prime(x)=nx**(n-1)
    for i in range:
        nroot=x_(i-1)-f(x_(i-1))/f_prime(x_(i-1))
    return (round(nroot(n,t,num),3))

def nroot_complex(n,t,num):
    j=(-1)**0.5
    if num>=0: 
        x**n=num
        f(x)=x**n-num
        f_prime(x)=nx**(n-1)
    elif num<0 and n%2==0:
         x**n=num
         f(x)=x**n-num
         f_prime(x)=nx**(n-1)
    elif num<0 and n%2!=0:
        x**n=num
        f(x)=x**n-num
        f_prime(x)=nx**(n-1)
    for i in range:
        nroot=x_(i-1)-f(x_(i-1))/f_prime(x_(i-1))
    
    return (round(nroot_complex(n,t,num),3))