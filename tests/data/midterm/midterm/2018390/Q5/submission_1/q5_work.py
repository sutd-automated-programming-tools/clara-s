import math

def f(x0, n, num):
    return (x0**n)-num
    pass

def f_dev(x0, n, num):
    return (x0*n)**(n-1)
    pass

def nroot(n,t,num):
    x0 = 1
    i = 1
    while i < t:
        x1 = x0 - f(x0,n,num) / f_dev(x0,n,num)
        x0 = x1
        i += 1
    return round(x0,3)
    pass

def nroot_complex(n,t,num):
    i = 1
    
    while i < t:
        if n % 2 == 0 and num < 0:
            abs_num = abs(num)
            x = nroot(n,t,abs_num)
            i += 1
            y = round(x,3)
            return y*1j
        
        elif n % 2 != 0 and num < 0:
            abs_num = abs(num)
            x = nroot(n,t,abs_num)
            i += 1
            y = round(x,3)
            return round(y*-1,3)
    pass