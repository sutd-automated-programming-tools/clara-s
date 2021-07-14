# MID-TERM EXAM: QUESTION 5

def f(x,n,num):
    return x**n - num

def fprime(x,n):
    return n* ( x** (n-1))

def nroot(n,i,num):
    x = 1
    for i in range(i):
        x -= f(x,n,num) / fprime(x,n)
    return round(x,3)

def nroot_complex(n,i,num):
    if num > 0:
        return nroot(n,i,num)
    elif num < 0:
        if n % 2 == 0:
            return nroot(n,i,abs(num)) * 1j
        else:
            return nroot(n,i,abs(num)) * (-1)
    else:
        return 0

print(nroot(2,5,2))
print(nroot_complex(2,5,-4))
print(nroot_complex(3,5,-8))   