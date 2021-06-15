# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    fx = i**2 - num
    fxp = 2*i
    ans = (i-1)-(fx/fxp)
    return round(ans,3)
    
def nroot_complex(n,i,num):
    x = i**2 - num
    fxp = 2*i
    ans = (i-1)-(fx/fxp)
    return round(ans,3)