def nroot(n,i,num):
    x = 1
    t = 0
    while t <= i:
        f_x = x ** n - num
        f_xx = n * (x **(n - 1)) 
        x = x - (f_x / f_xx)
        t += 1
    return round(x,3) 



        
def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0 and n % 2 == 0:
        x = nroot(n,i,abs(num)) * 1j 
        return x
    elif num < 0 and n % 2 != 0:
        x = nroot(n,i,abs(num)) * -1
        return x