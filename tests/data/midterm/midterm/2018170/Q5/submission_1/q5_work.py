# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for l in range (i):
        y = x**n - num
        y_p = n*x
        x = x-(y/y_p)
    return round(x,3)

def nroot_complex(n,i,num):
    if n%2 ==0:
        return str(nroot(n,i,num))+ 'j'
    else:
        if nroot(n,i,num)<=0 : 
            return nroot(n,i,num)
        else:
            return -nroot(n,i,num)