# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    loopvar = 0
    while loopvar <= t:
        fx = x**n - num
        fpx = n*(x**(n-1))
        x = x - (fx/fpx)
        loopvar+=1
    return round(x,3)

def nroot_complex(n,t,num):
    if num >=0:
        result = nroot(n,t,num)
    else:
        result = nroot(n,t,abs(num))
        if n%2 == 0:
            result = complex(0,result)
        else:
            result = -1*abs(result)
            
    return result