# MID-TERM EXAM: QUESTION 5

import cmath , math
def nroot(n,i,num):
    ans=num
    for j in range(1,n,1):
        ans=math.sqrt(ans)
    return round(ans,3)

def nroot_complex(n,i,num):
    Ans=0
    if num>0:
        Ans=nroot()
    elif num<0:
        if n%2==0:
            for j in range(1,n,1):
                Ans=cmath.sqrt(num)
        else:
            Ans = -(nroot(n,i,-num))
    return Ans
print(nroot_complex(2,5,-4))