# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=2
    for z in range(i):
        x=x-((x**n-num)/(n*x))
    return round(x,3)

def nroot_complex(n,i,num):
    if num<0:
        p_num=abs(num)
        if n%2==0:
            return(nroot(n,i,p_num)*1j)
        else:
            return(-nroot(n,i,p_num))
    elif num>0:
        return(nroot(n,i,num))
    else:
        return None