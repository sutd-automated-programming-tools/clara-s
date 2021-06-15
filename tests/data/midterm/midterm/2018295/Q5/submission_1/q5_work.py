# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    first=1-(1-num)/2
    for j in range(1,t+1):
        output=first-(first**n-num)/(n*(first)**(n-1))
        first=output
    return round(first,3)

def nroot_complex(n,t,num):
    pass