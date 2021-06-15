# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if num>0:
        root=(num)**0.5
        root=round(root,3)
        print(root)
        return(root)
def nroot_complex(n,t,num):
    if num>0:
        rootnroot(n,t,num)
        print(root)
        return(root)
    elif  n%2==0 and num<0:
        k=abs(num)
        new_root=(k)**0.5
        IROOT=1j*(new_root)
        print(IROOT)
        return IROOT
    elif n%2!=0 and num<0:
        k=abs(num)
        new_root=(k)**0.5//1
        new_root=round(new_root,0)
        new_root=-1*new_root
        print(new_root)
        return new_root