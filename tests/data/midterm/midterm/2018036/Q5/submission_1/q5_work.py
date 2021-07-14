def nroot(n,i,num):
    a = num**n
    fx = a-num
    fxp = n*(num)**(1/float(n))
    x=1
    for j in range(i):
        x = x - fx/fxp
        fx = x**n - num
        fxp = n*num**(1/float(n)
    return round(x,3)

def nroot_complex(n,i,num):
    if num<0 and n%2==0:
        x = nroot(n,i,num*-1)
        y = int(x*-1)
        return str(y)+'j'