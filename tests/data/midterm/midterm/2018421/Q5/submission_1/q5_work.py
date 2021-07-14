# MID-TERM EXAM: QUESTION 5

def nroot(n, t, num):
    ans=(num)**(1/n)
    ans=round(ans,3)
    return ans

def nroot(n, t, num):
    if num<0:
        False
    else: 
        x=1
        fx=(x**n)-num
        fxprime=n*x**(n-1)
        x=(x-1)-((fx)/(fxprime))  
        x+=1
        x=round(x,3)
        return x

def nroot_complex(n,t,num):
    pass