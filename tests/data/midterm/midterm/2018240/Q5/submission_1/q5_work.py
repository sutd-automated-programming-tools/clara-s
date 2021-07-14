def nroot(n,i,num):
    x=1
    count=1
    while count<i:
        x=x-(((x**n)-num)/(n*x))
        count+=1
    x=round(x,3)
    return x
    
def nroot_complex(n,i,num):
    a=0
    if num >=0:
        a=nroot(n,i,num)
    elif num<0 and n%2==0:
        a=nroot(n,i,(-1*num))*1j
    elif num<0 and n%2!=0:
        a=nroot(n,i,(-1*num))
    return a