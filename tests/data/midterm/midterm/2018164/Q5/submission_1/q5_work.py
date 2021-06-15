# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = num**(1/n)
    return round(x,3)
def nroot_complex(n,t,num):
    if n%2 == 0  :
        out = nroot(n,i,num) * 'j'
    else:
        out = nroot(n,i,num) * -1
    return round(out,3)