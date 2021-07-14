# MID-TERM EXAM: QUESTION 5

#def nroot(n,t,num):
#    pass

#def nroot_complex(n,t,num):
#    pass

def nroot(n, t, num):
    ans = 1
    if num == 0:
        return 0
    else:
        for a in range(t):
            ans = ans - (((ans**n)-num) / (2*ans))
        return round(ans, 3)
    
def nroot_complex(n, t, num):
    ans = 1
    if num == 0:
        return 0
    elif num < 0 and n%2 == 0:
        num = -1*num
        for a in range(t):
            ans = ans - (((ans**n)-num) / (2*ans))
        return round(ans, 3)*1j
    elif num < 0:
        num = -1*num
        return -1*nroot(n, t, num)
    else:
        nroot(n, t, num)