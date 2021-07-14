# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    iteration = 0
    x = 1
    while iteration < t:
        x -= (x**n - num)/(n*x**(n-1))
        iteration += 1
    return round(x,3)

def nroot_complex(n,t,num):
    if num >= 0:
        return nroot(n,t,num)
    else:
        if n%2 == 0:
            mag = nroot(n,t,-num)
            return mag * 1j
        else:
            return -nroot(n,t,-num)