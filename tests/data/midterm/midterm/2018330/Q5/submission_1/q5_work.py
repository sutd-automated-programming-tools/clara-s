# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    for tms in range(t):
        sq=num
        d0=sq-num
        d1=t-tms*(sq**(1/t-tms))
        sq= sq-(d0/d1)
    constant=sq
    return constant
     
    
    pass

def nroot_complex(n,t,num):
    constant= nroot(n,t,num)
    if n%2==0:
        out=str(constant) +"j"
        return out
    else:
        out="-"+ str(constant)
        return out