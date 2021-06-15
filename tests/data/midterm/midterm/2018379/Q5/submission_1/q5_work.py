# MID-TERM EXAM: QUESTION 5
import numpy as np
def nroot(n,t,num):
    x = 1
    for iteration in range(t):
        f = x**n - num
        ff = n*(x)**(n-1)
        x -= float(f)/ff  
    return (round(x,3)) 

def nroot_complex(n,t,num):
    if n % 2 == 0: #even
        x = 1
        for iteration in range(t):
            f = np.complex(x**n - num)
            ff = np.complex(n*(x)**(n-1))
            x -= f/ff
        return (np.complex(x))
    if n % 2 != 0:
        x = 1
        for iteration in range(t):
            f = x**n - num
            ff = n*(x)**(n-1)
            x -= f/ff
        return (round(x,3))