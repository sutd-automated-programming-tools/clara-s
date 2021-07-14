# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    a=0
    x=1
    while a<=t:
        x=x-(x**n-num)/((n)*x**(n-1))
        a+=1
    
    return round(x,3)
    while a<=t:
        x=x-(x**2-num)/(2*x)
        a+=1
    return round(x,3)

def nroot_complex(n,t,num):
    if num>=0:
        result=nroot(n,t,num)
    else:
        if n%2==0:
            result=complex(str(nroot(n,t,-num))+'j')
        else:
            result=nroot(n,t,-num)
            result=-result
    return result
            