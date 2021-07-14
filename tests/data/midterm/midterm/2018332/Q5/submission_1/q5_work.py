# MID-TERM EXAM: QUESTION 5
import math
def nroot(n,t,num):
    xi = 1
    for i in range(2,t+1):
        xi = xi - (xi**n - num)/(n*(xi**(n-1)))
    return round(xi,3)

def nroot_complex(n,t,num):
    if n % 2 == 0:
        num_positive = abs(num)
        return nroot(n,t,num_positive)*1j
    else:
        return nroot(n,t,num)
        