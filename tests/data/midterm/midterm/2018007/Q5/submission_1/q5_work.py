# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    x = 1
    fx = x**n - num
    fx1 = n*x**(n-1)
    for i in range(i):
        x_i = x - fx/fx1
        x = x_i
        fx = x_i**n - num
        fx1 = n*x_i**(n-1)
    
    return round(x,3)

def nroot_complex(n,i,num):
    if num >= 0:
        return nroot(n,i,num)
    elif n%2 != 0:
        num = -num
        result = nroot(n,i,num)
        result = -result
        return result
    elif n%2 == 0:
        num = -num
        result = nroot(n,i,num)
        result = result*1j
        
        return result