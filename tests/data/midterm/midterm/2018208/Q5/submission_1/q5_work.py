def nroot(n,i,num):
#    x = (num)**(1/n)
#    fx = x**n - num
#    fprimex = n*x**(n-1)
    xans = (num)**(1/n)
    for j in range(i):
        xans = xans - fx(xans,n,num)/fprimex(xans,n)
    if type(xans) != complex:
        return round(xans,3)
    else:
        return xans
    
def x(n, num):
    return (num)**(1/n)
def fx(x,n,num):
    return x**n - num
def fprimex(x,n):
    return n*x**(n-1)

def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0 and n%2 == 0:
        return nroot(n,i,num)
    elif num < 0 and n%2 == 1:
        return abs(nroot(n,i,num))