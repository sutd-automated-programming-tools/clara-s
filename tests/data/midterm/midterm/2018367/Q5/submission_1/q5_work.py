import numpy as np


def nroot(n,i,num):
    x = 1
    if n == 2:
        for k in range(i):
            x = x - (x**2-num)/(2*x)
            k += 1
    if n == 3:
        for k in range(i):
            x = x - (x**3-num)/(3*x**2)
            k += 1
    return round(x,3)

def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,num)
    else:
        if n%2==0:
            num = -num
            ans = nroot(n,i,num)
            ans = ans*(-1)**0.5
            ans = ans - np.real(ans)
            return ans
        else:
            num = -num
            ans = -nroot(n,i,num)
            return ans
