# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    if num == 0:
        return num
    x = 1
    for j in range(i):
        x = x - ((x**n) - num)/(n*x**(n-1))
        print(x)
    return round(x,3)
#print(nroot(2,5,2))

def nroot_complex(n,i,num):
    if num == 0:
        return num

    if num > 0:
        return nroot(n,i,num)
    elif n%2 == 0:
        return nroot(n,i,-num)*1j
    else:
        return nroot(n,i,num)