# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    return round(num**0.5,3)

def nroot_complex(n,i,num):
    if num >= 0:
        return nroot(n,i,num)
    if num <= 0 and n%2 == 0:
        num = abs(num)
        return str(int(nroot(n,i,num))) + 'j'
    if num <= 0 and n%2 != 0:
        num = abs(num)
        return -int(nroot(n,i,num))