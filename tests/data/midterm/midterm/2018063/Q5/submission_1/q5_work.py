# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    denial = 1
    i = 0
    while i < t:
        denial -= (denial**n-num)/(n*denial**(n-1))
        i += 1
    return round(denial,3)
        

def nroot_complex(n,t,num):
    if num >= 0:
        return nroot(n,t,num)
    if n%2 ==0:
        return nroot(n,t,-num)*1j
    return -nroot(n,t,-num)
    