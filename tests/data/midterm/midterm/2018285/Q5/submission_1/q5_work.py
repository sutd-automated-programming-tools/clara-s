# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for j in range(0,i):
        f = x**n - num
        f_prime = n*x**(n-1)
        x = x-(f)/(f_prime)
        
    return round(x,3)

def nroot_complex(n,i,num):
    if n %2 == 0:
        return nroot(n,i,-num)*1j
    else:
        return -nroot(n,i,-num)
