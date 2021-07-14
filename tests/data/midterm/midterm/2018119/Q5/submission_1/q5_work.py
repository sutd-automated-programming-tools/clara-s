# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    ximinus1 = 1
    while i != 0:
        yiminus = ximinus1**n - num
        yprimeiminus1 = n*ximinus1**(n-1)
        xi = ximinus1 - (yiminus/yprimeiminus1)
        i -= 1
        ximinus1 = xi
    ximinus1 = round(ximinus1,3)
    return ximinus1

def nroot_complex(n,t,num):
    x = num*-1
    output = nroot(n,t,x)
    output = output*1j
    return output