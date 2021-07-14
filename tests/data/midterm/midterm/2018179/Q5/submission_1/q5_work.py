# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for k in range(t):
        fx = x ** n - num
        f_x = n * x ** (n-1)
        x -= fx / f_x
    return round(x,3)

def nroot_complex(n,t,num):
    numt = -1*num
    ans = nroot(n, t, numt)
    if num < 0 and n%2 == 0:
        return ans*1j
    elif num < 0 and n%2 != 0:
        return -1*ans