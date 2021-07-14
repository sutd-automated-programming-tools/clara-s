# MID-TERM EXAM: QUESTION 5

import cmath

def nroot(n,i,num):
    root= (num)**(1/n)
    return round(root,3)


def nroot_complex(n,i,num):
    if num>0:
        return nroot(n,i,num)
    if num<0:
        if n%2==0:
            root2=(-num)**(1/n)*1j
        else:
            root2=-(-num)**(1/n)
        return root2
            
     