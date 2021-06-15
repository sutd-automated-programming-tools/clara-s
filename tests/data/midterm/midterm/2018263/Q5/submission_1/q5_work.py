# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    re=num**(1.0/n)
    return round(re,3)
    pass

def nroot_complex(n,t,num):
    if num>=0:
        ans=f(n,t,num)
    else:
        if n%2!=0:
            ans=round(num**(1.0/n),3)
        else:
            ans=num**(1.0/(-n))
            ans=0+1j*ans
    return ans
    pass