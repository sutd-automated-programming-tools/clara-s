# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    xi = num**0.5
    for i in range(1,t+1):
        xi = xi - func(xi,num)/deriv(xi)
    if xi.imag == 0:
        return round(xi,3)
    else:
        return xi

def func(x, num):
    return x**2 - num

def deriv(x):
    return 2*x

def nroot_complex(n,t,num):
    if num < 0 and num%2 == 0:
        ans = nroot(n,t,num)
        return ans.imag * 1j
    elif num < 0 and num%2 != 0:
        ans = nroot(n,t,num)
        return round(ans.real,3)