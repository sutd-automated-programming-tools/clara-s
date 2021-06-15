# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x0 = 1
    i = 1
    while i < t:
        func1 = x0**n - num
        func2 = n*(x0**(n-1))
        x0 = x0 - (func1/func2)
        i += 1
    return round(x0,3)
    

def nroot_complex(n,t,num):
    if num < 0 and n%2==0:
        #case 2, complex with no real part
        const=nroot(n,t,num*(-1))
        return const*1J
        
    elif num < 0 and n%2!=0:
        #case 3, negative real number
        const=nroot(n,t,num*(-1))
        return const*(-1)