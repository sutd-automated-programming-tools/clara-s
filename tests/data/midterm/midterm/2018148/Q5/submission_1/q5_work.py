# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    x = 1
    if num >= 0:
        for root in range (1,n+1):
            for iteration in range(i):
                f = x**2 - num
                dif = 2*x
                x = x-f/dif
    return round(x,3)

def nroot_complex(n,i,num):
    if num >= 0:
        return nroot(n,i,num)
    else:
        if n/2 == int:
            return -nroot(n,i,abs(num))
        else:
            num = abs(num)
            ans = complex(0,nroot(n,i,num))
            return ans