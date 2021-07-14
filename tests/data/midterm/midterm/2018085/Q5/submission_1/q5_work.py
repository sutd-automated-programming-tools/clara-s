# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    exp1=x**n-num
    exp2=n*x
    for j in range(i):
        z=x**n-(exp1)/(exp2)
        if j>0:
            exp1=z**(n)-num
            exp2=z*n
            z=z**n-((exp1)/(exp2))
    return round(z,3)

def nroot_complex(n,i,num):
    if num/-1<0:
        return nroot(n,i,num)
    if n%2==0:
        x=int(nroot(n,i,-num))*1j
        return x
    else:
        return nroot(n,i,-num)