def nroot(n,t,num):
    
    start = 1
    fx = x**n - num
    fx_ = n*x**(n-1)
    ans = fx/fx_
    while start < t:
        ans = ans-fx/fx_
        start+=1
    return ans
        

def nroot_complex(n,t,num):
    pass
