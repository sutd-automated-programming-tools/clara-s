# MID-TERM EXAM: QUESTION 5

j=(-1)**0.5

def nroot(n,t,num):
    root = (num)**(1/n)
    return round(root,3)

def nroot_complex(n,t,num):
    if num%2 ==0:
        return nroot(n,t,num)*j
    if num%2 !=0:
        return -nroot(n,t,num)*j