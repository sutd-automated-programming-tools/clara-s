# MID-TERM EXAM: QUESTION 5
import cmath

def nroot(n,t,num):
    x = 1
    count = 0
    if num == 0:
        return 0
    while count < t:
        fx = x**n - num
        dfx = n*x**(n-1)
        x = x-(fx/dfx)
        count += 1
    return round(x,3)

def nroot_complex(n,t,num):
    j = cmath.sqrt(-1)
    if num >= 0:
        val = nroot(n,t,num)
        return val
    elif num < 0 and n%2 == 0:
        val = nroot(n,t,-num)*j
        return val
    elif num < 0 and n%2 != 0:
        val = -nroot(n,t,-num)
        return val