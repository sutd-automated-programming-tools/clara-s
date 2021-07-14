# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    
    x = num**(1/n)
#    f = x**n - num
#    fprime = n*(x**(n-1))
    
    return round(x, 3)


def nroot_complex(n,t,num):
    x= 1
    for j in range(2,n+1):
        f = x**(j-1)
        fprime = (j-1)*(x**(j-2))
        x = x - (f/fprime)
        
        
    return x