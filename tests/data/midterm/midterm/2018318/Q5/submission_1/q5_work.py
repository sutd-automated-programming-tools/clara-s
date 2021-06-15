# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num): #positive num
    x=1
    x=num**(1/n)
    f= x**n -num
    fprime=n*x**(n-1)
    approx = x - f/fprime
    
    return (round(approx,3))

def nroot_complex(n,t,num):#negative num
    
    output=nroot(n,t,num)
    return (round(output,3))
