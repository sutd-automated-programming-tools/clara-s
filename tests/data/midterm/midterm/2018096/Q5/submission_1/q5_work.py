# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    if num > 0:
        x = (num)**0.5
        return round(x,3)
    else:
        nroot_complex(n,t,num)

def nroot_complex(n,t,num):
    if num > 0:
        x = nroot(n,t,num)
        return x
    if num < 0:
        number = num*(-1)
        x = nroot(n,t,number)
        
        if n%3 == 0:
            z = x*(-1)
            return z
        if n%2 == 0:
            root = x*(1j)
            return root
    
#square root of 8 is not 2?
    