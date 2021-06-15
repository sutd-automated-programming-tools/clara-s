# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    ans = 1
    for i in range(0,t):
        ans = ans - (ans**n-num)/(n*ans)
        return round(ans,3)
        
        
    

def nroot_complex(n,t,num):
    pass