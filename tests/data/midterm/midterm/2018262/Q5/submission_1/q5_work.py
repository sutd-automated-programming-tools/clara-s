# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(n+1):
        f = x**n - num
        f_prime = n*x
        x -=  f/f_prime
    return round(x,3)


def nroot_complex(n,t,num):
    pass