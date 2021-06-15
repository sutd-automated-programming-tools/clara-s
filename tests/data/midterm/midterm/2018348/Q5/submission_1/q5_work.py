# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    for j in range(1,i +1):
        fxmo = x**n - num
        fpxmo = n*x**(n-1)
        y = x - fxmo/fpxmo
        x = y
    return round(x,3)

print(nroot(2,5,4))
def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num == 0:
        return 0
    else:
        if n%2 == 0:
            return nroot(n,i,-num)*1j
        else:
            return nroot(n,i,-num)*-1