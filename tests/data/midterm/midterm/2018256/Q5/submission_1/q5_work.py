# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    c = 1
    while c < n+1:
        c += 1
        fx = x**n - num
        fx_prime = n*x**(n-1)
        x = round(x - fx / fx_prime, 3)
    return x

def nroot_complex(n,t,num):
    if n%2==0:
        num = -1*num
        ans = nroot(n,t,num)
    else:
        
    pass