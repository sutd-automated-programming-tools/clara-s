# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    sqX = num**2
    funX = sqX - num
    funPrimeX = 2* (sqX)**0.5
    
    eqn = 1
    for i in range(t+1):
        eqn -= (funX / funPrimeX)
    return eqn


def nroot_complex(n,t,num):
    pass