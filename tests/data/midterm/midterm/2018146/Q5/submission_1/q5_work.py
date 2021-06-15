# MID-TERM EXAM: QUESTION 5
def nroot(n,t,num):
    x=1
    for j in range(1,t+1):
        x1=x-(x**2-num)/(2*x)
        x=x1
    return round(x,3)

def nroot_complex(n,t,num):
    if num>=0:
        return nroot(n,t,num)
    elif num<0 and n%2!=0:
        r1=int(nroot(n,t,-num))
        r=-r1
        return r
    elif num<0 and n%2==0:
        r1=int(nroot(n,t,-num))
        r=r1
        return complex(0,r)