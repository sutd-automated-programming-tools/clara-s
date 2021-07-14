# MID-TERM EXAM: QUESTION 5
import math
def nroot(n, i, num):
    x = num**(1/n)
    xi = x**i
    f_x = xi - num
    fprime = i*x
    result = xi - f_x/fprime
    return round(result, 3)
    
    
def nroot_complex(n, i, num):
    x = nroot(n, i, num)