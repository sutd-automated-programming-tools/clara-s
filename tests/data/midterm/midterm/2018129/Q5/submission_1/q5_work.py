def nroot(n,i,num):
    x = 1
    for ai in range(1,i+1):
        x = x - (x**n-num)/(n*x**(n-1))
    return round(x,3)
    
def nroot_complex(n,i,num):
    if n % 2 == 0:
        ans = nroot(n,i,num*-1)
        return ans*1j
    else:
        ans = nroot(n,i,num*-1)
        return ans*-1