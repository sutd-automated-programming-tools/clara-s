# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    return round(num**(1/n),3)

def nroot_complex(n,t,num):
    #NR approx for negative num
    x=1
    fx=x**n-num
    fprime=n*x**(n-1)
    for number in range(t+1):
        x=x-fx/fprime