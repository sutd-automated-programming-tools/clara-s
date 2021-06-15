def nroot(n,t,num):
    x=1
    i=0
    while i<t:    
        x=x-(x**n-num)/(n*x)
        i+=1
    return round(x,3)

def nroot_complex(n,t,num):
    if num>0:
        return nroot(n,t,num)
    if num<0:
        if n%2!=0:
            return nroot(n,t,num)
        else:
            return nroot(n,t,-num)*1j