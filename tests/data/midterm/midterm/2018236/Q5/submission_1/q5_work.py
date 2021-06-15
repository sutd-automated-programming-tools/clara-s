# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    xi = 1
    while t >0:
        xi = xi - (xi**n - num)/(n*xi**(n-1))
        t -= 1
    ans = round(xi, 3)
    return ans

def nroot_complex(n,t,num):
    if num  >= 0:
        return nrrot(n,t,num)
        
    if n%2 == 0:
        return nroot(n,t,abs(num))*1j
    elif n%2 == 1:
        return nroot(n,t,abs(num))*(-1)
    