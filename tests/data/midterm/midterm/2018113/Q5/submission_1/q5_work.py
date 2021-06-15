# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(t):
        x -= (x**n - num)/(n*x**(n-1))
    return round(x,3)
       

def nroot_complex(n,t,num):
    if num < 0:
        abso = nroot(n,t,abs(num))
    else:
        return nroot(n,t,num)
    if n%2 == 0:
        return abso*1j
    else:
        return abso*(-1j)
       