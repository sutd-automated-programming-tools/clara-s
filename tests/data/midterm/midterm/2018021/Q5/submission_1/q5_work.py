# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x0 = 1
    x1 = x0 - ((x0 ** n) - num) / (n * (x0 ** (n - 1)))
    count = n - 1
    for a in range(1, i):
        x = x - (x ** count - num) / (n * x ** (count - 1))
        count -= 1
    return x
def nroot_complex(n,t,num):
    pass