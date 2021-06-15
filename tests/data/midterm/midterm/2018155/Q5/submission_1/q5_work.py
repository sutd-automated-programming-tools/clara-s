# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    
    x = num ** (1/n)
    fx = x**n - num
    dx = n * x ** (n-1)
    for h in range(t):
        newx = x - fx/dx
        x = newx
    return round(newx,3)

def nroot_complex(n,t,num):
    newnum = -num
    value = nroot(n,t,newnum)
    if n%2 == 0:
        ans = value * 1j
    else:
        ans = -1 * value
    return ans