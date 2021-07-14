# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    for k in range(i):
        x=x-(x**n-num)/(n*x**(n-1))
    x=round(x,3)
    return x


def nroot_complex(n,t,num):
    x=1
    if num >= 0:
        x=nroot(n,t,num)
        return x
    elif num < 0:
        if n%2!=0:
            for k in range(t):
                x=x-(x**n-num)/(n*x**(n-1))
                x=round(x,3)
                
            return x
        if n%2 ==0:
            for k in range(t):
                x=x-(x**n-num)/(n*x**(n-1))
                x=round(x,3)
                a=x*1j
            return a