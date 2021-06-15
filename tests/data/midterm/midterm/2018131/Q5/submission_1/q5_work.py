# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    
    for c in range(i):
        fx=x**n-num
        fpx=n*(x**(n-1))
        x=x-(fx/fpx)
        print(x)
    
    return round(x,3)

def nroot_complex(n,i,num):
    
    if num<0 and (n%2)==0:
        mag=nroot(n,i,abs(num))
        root=complex()
        root=mag*1j
        return root
    if num<0 and n%2!=0:
        mag=nroot(n,i,abs(num))
        root=-1*mag
        return root
    else:
        return nroot(n,i,num)