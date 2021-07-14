# MID-TERM EXAM: QUESTION 5

import cmath as c
def nroot(n,i,num):
    x = 1
    fx = i
    fp = i-1
    for idx in range(1,i):
        x = x**fx - ((x**fx)-num)/(fx*(x**fp))
        print(x)

print(nroot(2,5,2))


def nroot_complex(n,t,num):
    pass