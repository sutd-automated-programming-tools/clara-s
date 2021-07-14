# MID-TERM EXAM: QUESTION 5

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

#print(iseven(-9))

def nroot(n,i,num):
    x=1
    for k in range(i):
        x=x-(((x**n)-num)/(n*x**(n-1)))
    return round(x,3)

#print(nroot(2,5,2))

def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,num)
    elif num<0 and is_even(n)==False:
        return -1*nroot(n,i,-num)
    elif num<0 and is_even(n)==True:
        return nroot(n,i,-num)*1j