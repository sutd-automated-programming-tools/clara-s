# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    root=num**(n/2)
    return root

def nroot_complex(n,i,num):
    if num > 0:
        root1=nroot(n,i,num)
        return root1
    if num < 0:
        root=num**(1/n)
        return abs(root)
        

    