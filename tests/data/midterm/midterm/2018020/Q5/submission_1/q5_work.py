# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    if num >= 0:
        x = (num)**(1/n)
        
    return round(x,3)
        
def nroot_complex(n, i, num):
    if num <= 0 and n % 2 == 0:
        xeven = nroot(n, i, -num)
        ceven = xeven * 1j
        out = ceven
        
    elif num <= 0 and n % 2 != 0:
        xodd = nroot(n, i,-num)
        codd = xodd * -1
        out = codd
        
    elif num >= 0:
        cpos = nroot(n, i,num)
        out = cpos
    
    return out