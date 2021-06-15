# MID-TERM EXAM: QUESTION 5

from math import sqrt
def nroot(n,t,num):
    x_2 = num
    x = sqrt(x_2)
    for k in range(0,t):
        f_x = x_2 - num
        f_prime = n*x
        x = x - f_x/f_prime
    return round(x,3)

def nroot_complex(n,t,num):
    if num > 0:
        return nroot(n,t,num)
    elif num%2 is 0:
        return nroot(n,t,-num)*1j
    else:
        return -nroot(n, t, -num)