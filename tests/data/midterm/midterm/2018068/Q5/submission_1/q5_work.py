# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    i = 1
    while i<t:
        x2 = x**n
        fx = x**n - num
        f1x = n*x**(n-1)
        x = x - fx/f1x
        i+= 1
    return round(x,3)

def nroot_complex(n,t,num):
    if num <0 and n%2 == 0:
        num = abs(num)
        ans = nroot(n,t,num)
        ans = ans*1j
    elif num <0 and n%2 ==1:
        num = abs(num)
        ans = nroot(n,t,num)
        ans = ans*(-1)
        ans = round(ans,1)
        
    return ans
    pass