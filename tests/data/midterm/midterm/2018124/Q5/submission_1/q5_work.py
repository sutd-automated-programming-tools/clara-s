# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):       
    x = 1
    for i in range(n,0,-1):
        fx = x**n - num
        fxprime = n*(x**(n-1))
        x -= fx/fxprime
    return round(x,3)

def nroot_complex(n,t,num):
    if num > 0:
        return round(nroot(n,t,num),3)
    elif num<0:
        if num %2 ==0:
            constant = nroot(n,t,-num)
            return constant*1j
        else:
            return nroot(n,t,num)+nroot(n,t,-num)*1j