# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = num**(1/n)
    for j in range(i):
        
        x = x - (x**2-num)/(2)
        j = j+1
    return x

def nroot_complex(n,i,num):
    z = 0
    if num < 0 and num % 2 ==0:
        
        z.imag = nroot(n,i,num)
        return z
    elif num < 0 and num% 2 != 0:
        return -nroot(n,i,num)