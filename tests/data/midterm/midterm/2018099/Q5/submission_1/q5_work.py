# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x=1
    x= num**0.5
    fx=x**2-num
    fxprime=2*x
    xi= round (x- (fx/fxprime),3)
    return xi

def nroot_complex(n,t,num):
    x=1
    j=(-1)**0.5
    if (num>0):
        output= nroot(n,t,num)
    elif (num>0) and (n%2==0):
        output= nroot(n,t,num)
    elif (num<0) and (n%2!=0):
        num*j
        output= nroot(n,t,num)
        return output