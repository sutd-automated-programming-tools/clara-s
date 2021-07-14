def nroot(n,i,num):
    x = 1
    for i in range(i):
        
        fx = x**n - num
        f_prime = n*x**(n-1)
        x = x - fx/f_prime
    return round(x,3)

def nroot_complex(n,i,num):
    if num < 0 and n%2 != 0:
        return -nroot(n,i,-num)
    if num >= 0:
        return nroot(n,i,num)
    if num < 0 and n%2 == 0:
        return nroot(n,i,-num)*1j
print(nroot(2,5,2))
print(nroot_complex(3,5,-8))
