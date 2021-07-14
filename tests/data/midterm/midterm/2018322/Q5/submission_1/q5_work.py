def nroot(n,i,num):
    x=num**0.5
    while i>=0:
        fx = x**2-num
        fprimex = 2 * (x)
        x = x - fx/fprimex
        i-=1
        return round(x,3)

    
def nroot_complex(n, i, num):
    if num>0:
        return None
    
    else:
        if n%2== 0:
            positive = num * (-1)
            value = nroot(n,i,positive) * 1j
            return value
        
        else:
            positive = num * (-1)
            value = positive **(1 / n) *(-1)
            return round(value,3)