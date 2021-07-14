# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num): #root of non -ve num
    c = 0
    oldx = num**(1/n)
    fx = x**n - num
    dy = n * x**(n-1)
    part = fx/dy
    while c < i:
        x = x - part
        c += 1
    
def nroot_complex(n,i,num): #root of -ve num