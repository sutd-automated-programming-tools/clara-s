# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    x = 1
    for count in range(i):
         f = x**n-num
         df = n*x**(n-1)
         x -= f/df
    return round(x, 3)
    
def nroot_complex(n, i, num):
    if num >= 0:
        return nroot(n, i, num)
    elif num < 0 and n % 2 == 0:
        return nroot(n, i, -num)*1j
    elif num < 0 and n%2 != 0:
        return -nroot(n, i, -num)