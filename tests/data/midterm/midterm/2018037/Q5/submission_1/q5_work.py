# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    a=0
    res = num-(((num)**n-num)/((n)*num**(n-1)))
    while a < i:
        res = res-((res)**n-num)/((n)*res**(n-1))
        a+=1
    return round(res,3)

def nroot_complex(n,i,num):
    pnum = -1*num
    real = nroot(n,i,pnum)
    if n%2 == 0:
        return real*1j
    else:
        return real*-1