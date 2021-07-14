# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = num ** (1/n)
    c = x
    a = x**n - num
    b = n * x**(n-1)
    k = 0
    
    while k < i:
        c = c - (a/b)
        k += 1
    
    return round(c,3)

def nroot_complex(n, i, num):
    a = -num
    b = nroot(n,i,a)
    
    if n%2 == 0:
        return (str(int(b)) + "j")
    else:
        return (-float(b))