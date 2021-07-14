# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    oup = num**(1/n)
    return round(oup,3)

def nroot_complex(n,t,num):
    if n%2 == 0:
        root = nroot(n,t,-num)
        oup = str(int(root))+'j'
    if n%2 != 0:
        root = nroot(n,t,-num)
        oup = -root
    return oup
        
        
    