def nroot(n,i,num):
    count=0
    x=1
    
    while count<i:
        f=x**n-num
        df=n*x**(n-1)
        x=x-f/df
        count+=1
    return round(x,3)


           
def nroot_complex(n,i,num):
    
    if num>0:
        return nroot(n,i,num)
    elif num<0 and n%2!=0:
        count=0
        x=1
        
        while count<i:
            f=x**n-num
            df=n*x**(n-1)
            x=x-f/df
            count+=1
        return round(x,3)
    
    elif num<0 and n%2==0:
        count=0
        x=1
        num=-num
        while count<i:
            f=x**n-num
            df=n*x**(n-1)
            x=x-f/df
            count+=1
        return round(x,3)*1j