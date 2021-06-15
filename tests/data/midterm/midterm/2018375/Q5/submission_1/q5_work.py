# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    for x in range(i)
        if i == 1:
            y = 1
        if i > 1:
            y += y - (y**n - num)/(n*y**(n-1))
    return y
        
#sorry i don't understand the math
        
def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0 and n%2 == 0:
        return nroot(n,i,num) * 1j
    elif num < 0 and n%2 != 0:
        return -nroot(n,i,num)