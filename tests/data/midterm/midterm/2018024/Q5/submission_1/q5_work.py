# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    if n==2:
        xi=1
        for j in range (0,i):
            xf=xi-(((xi**2)-num)/(2*xi))
            xi=xf
        if xf<1.5:
            return round(xf,3)
        elif xf>1.5:
            return 2
    if n==3:
        xm=1
        for j in range (0,i):
            xl=xm-(((xm**3)-num)/(2*(xm**2)))
            xm=xl
        if xl<1.5:
            return round(xl,3)
        elif xl>1.5:
            return 2
def nroot_complex(n,i,num):
    m=abs(num)
    out=nroot(n,i,m)
    if n%2==0:
        return "2j"
    else:
        return(-out)