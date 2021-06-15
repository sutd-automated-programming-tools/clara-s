# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
#    x = (num)** (1/n) #find out x
#    f = (x ** n) - num #function of x
#    fd = n * (x ** (n-1)) #derivative of x
    x = 1
    i = 0
    while i <= t:
        x = x - (((x**n) - num)/(n *(x**(n-1))))
        i += 1
    return round (x, 3)

def nroot_complex(n,t,num):
    x = 1
    if num > 0:
        i = 0
        while i <= t:
            x = x - (((x**n) - num)/(n *(x**(n-1))))
            i += 1
        return round (x, 3)
    elif num<0 and n % 2 == 0:
        i = 0
        while i <= t:
            x = x - (((x**n) - num)/(n *(x**(n-1))))
            i += 1
        return round(x,0) , "j"
    
    elif num<0 and n % 2 != 0:
        i = 0
        while i <= t:
            x = x - (((x**n) - num)/(n *(x**(n-1))))
            i += 1
        return round (x, 0)