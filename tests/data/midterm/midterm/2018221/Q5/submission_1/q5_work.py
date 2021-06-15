# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = (num)**(1/n)
    return x,round(x,3)

def nroot_complex(n,t,num):
    if num%2 == 0:
        return(