# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    return round(num**(1/n),3)

def nroot_complex(n,t,num):
    if (-num)**(1/n) > 0:
        return round(-(-num)**(1/n),3)
    else:
        return complex(0,(-num)**(1/n))

def 