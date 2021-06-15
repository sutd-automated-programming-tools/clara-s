# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    if num >=0:
        x=1
        a=1
        while a<=i:
            fx=x**n-num
            f_pri=n*x**(n-1)
            x=x-fx/f_pri
            a+=1
    return round(x,3)

print(nroot(2,5,2))

def nroot_complex(n , i , num):
    if num>=0:
        return nroot(n,i,num)
    else:
        new_root=nroot(n,i,abs(num))*(1j**(n-1))
        return new_root
print(nroot_complex(3,5,-8))
    