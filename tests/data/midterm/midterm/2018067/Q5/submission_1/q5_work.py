# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x =1
    for i in range((t)+1):
        x = x - (((x**n) - num)/(n*(x**(n-1))))
    x= round(x,3)
    return x
    

def nroot_complex(n,t,num):
    if num > 0:
        ans = nroot(n,t,num)
        return ans
    elif num <0 and num%2 ==0:
        ans = nroot(n,t,-num)
        return ans 
    elif num < 0 and num % 2 != 0:
        ans = nroot(n,t,-num)
        ans = -1*ans
        return ans
    else:
        return None
        
    pass