# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    result = 0
    num = num / i
    x = (num)**(1/n)
    fx = x**n - num
    fprimex = n*x**(n-1)
    for y in range(i):
        result = result - fx/fprimex
        print (result)
    return result
def nroot_complex(n,t,num):
    