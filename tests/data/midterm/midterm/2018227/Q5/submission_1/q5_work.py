# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    n=1
    root=1
    while n<=t:
        
        fx=root**2 - num
        fxx=n*root
        root = root- (fx/fxx)
        n+=1
    return round(root,3)
    

def nroot_complex(n,t,num):
    if num>0:
        return nroot(n,t,num)
     if num<0 and n%2==1:
        num = complex(num,0)
        n=1
        root=complex(1,0)
        while n<=t:
            fx=root**2 - num
            fxx=n*root
            root = root- (fx/fxx)
            n+=1
            print(root)
        return (root - root.real)