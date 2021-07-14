# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    if i==1:
        x = 1
        fx = x**n - num
        fpx = n*(x**(n-1))
        return (x - (fx/fpx))
    else:
        a = nroot(n,i-1,num)
        fa = a**n-num
        fpa = n*(a**(n-1))
        return round((a - (fa/fpa)),3)


def nroot_complex(n,i,num):
    if num<0 and n%2==0:
        x = nroot(n,i,-num)
        return x*1j
    if num<0 and n%2!=0:
        x = nroot(n,i,-num)
        return -x