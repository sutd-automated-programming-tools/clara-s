# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = num**(1/n)
    x_ = x**n - num
    x__ = n*x**(n-1)
    final = x - x_/x__
    return round(final,3)

def nroot_complex(n,t,num):
    final = nroot(n,t,num)
    return final