# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = num**(1/n)
    count = 1
    while count <= t:
        x = x - ( (x**n - num)/(n*x) )
        count += 1
    return x

def nroot_complex(n,t,num):
    pass