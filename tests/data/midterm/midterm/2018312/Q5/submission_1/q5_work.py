# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x= num**(1/n)
    return round(x,3)
    

def nroot_complex(n,t,num):
    num =abs(num)
    x = nroot(n,t,num)
    if n%2==0:
        ans = '%dj'%x
        return (ans)
    if n%2!=0:
        return (-x)