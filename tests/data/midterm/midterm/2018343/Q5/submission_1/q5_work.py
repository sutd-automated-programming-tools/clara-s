# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    a=num
    for i in range(i):
        a=a-(a**n-num)/(n*a**(n-1))
    return round(a,3)

def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,num)
    elif num<0 and n%2==0:
        return nroot(n,i,-num)*1j
    elif num<0 and n%2!=0:
        return -nroot(n,i,-num)