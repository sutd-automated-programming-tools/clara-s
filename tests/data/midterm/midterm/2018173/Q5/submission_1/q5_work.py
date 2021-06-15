# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    m = 0
    while m < t:
        f = x**n - num
        fprime =n*x**(n-1)
        x = x - (f/fprime)
        m += 1
    return round(x,3)

def nroot_complex(n,t,num):
    if n%2 == 0:
        return (nroot(n,t,-num)*1j)
    else:
        return (-nroot(n,t,-num))