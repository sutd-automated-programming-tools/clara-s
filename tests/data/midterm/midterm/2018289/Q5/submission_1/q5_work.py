# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    #x = 1
    t1 = 0
    for x in range(1,t+1):
        while t1 <= t:
            fx = x**2 - num
            fxx = 2*x
            x1 = x - fx/fxx
            #x = x1
            t1+=1
    return x1

def nroot_complex(n,t,num):
    return nroot(n,t,num)