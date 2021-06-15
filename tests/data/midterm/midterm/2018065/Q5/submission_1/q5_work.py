# MID-TERM EXAM: QUESTION 5

  
def nroot(n,i,num):
    k = 0
    x = num
    
    while k<=i:
        x = x-((x**n-num)/(n*x**(n-1)))
        k+=1
    return round(x,3)

def nroot_complex(n,i,num):
    if n%2 ==0 and num<0:
        ans = str(round(nroot(n,i,(num*(-1))),3)) +'j'
        return ans
    else:
        ans = nroot(n,i,num)
        return round(ans,3)