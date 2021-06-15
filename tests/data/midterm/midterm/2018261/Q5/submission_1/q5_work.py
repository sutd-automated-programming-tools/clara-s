# MID-TERM EXAM: QUESTION 5
def nroot(n,t,num):
    x=1
    fun = x**n - num
    dev = n*x
    x = x - (fun/dev)
    n=n-1
    t=t-1
    if n ==0:
        break
    else:
        itera = nroot(n,t,x)
        x = itera
    
    return x


def nroot_complex(n,t,num):
    nroot(n,t,num)
    if n>=0:

    elif n<0 and n%2==0:

    elif n<0 and n%2!=0:
