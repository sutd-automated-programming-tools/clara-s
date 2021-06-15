# MID-TERM EXAM: QUESTION 5
import math

def nroot(n , i , num):
    def f(x):
        return (x ** n) - num
    def pf(x):
        return n * (x ** (n - 1))
    
    x = 1
    for r in range(i + 1):
        x = x - f(x)/pf(x)
    
    return round(x, 3)

def nroot_complex(n , i , num):
    x = nroot(n , i , abs(num))
    x = round(x, 3)
    if num < 0 and n%2 ==0:
        x = x * 1j
    elif num < 0:
        x = -x
    return x