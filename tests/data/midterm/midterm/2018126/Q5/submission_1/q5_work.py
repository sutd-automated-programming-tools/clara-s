def nroot(n, i, num):
    x = num
    f = lambda x: x ** n - num
    f_prime = lambda x: n * x ** (n - 1)

    for _ in range(i):
        ans = x - f(x) / f_prime(x)
        x = ans
        
    return round(ans, 3)
        
def nroot_complex(n, i, num):
    
    ans = nroot(n, i, -num)
        
    # if n is even
    if n % 2 == 0:
        ans = ans * 1j
    else:
        ans = -ans
    
    return ans