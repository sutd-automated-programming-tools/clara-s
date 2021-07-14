# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    c = 1
    x = 1
    while c < i:       
        x = x - (x**n - num) / (n * x)
        c += 1
    return round(x,3)

def nroot_complex(n,i,num):
    if num < 0 and n%2 ==0:
        out = nroot(n,i,-num)
        root = out * 1j
        return root
    elif num < 0 and n % 2 !=0:
        out = nroot(n,i,num) 
        root = out
        return root