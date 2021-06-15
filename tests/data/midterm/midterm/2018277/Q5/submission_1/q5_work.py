# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    for times in range(i):
        num = num - (num**n-num)/(n*num**(n-1))
    return num
def nroot_complex(n,i,num):
    if num<0 and num%2==0:
        num = -num
        return nroot(n,i,num)*1j
    if num<0 and num%2!=0:
        return -nroot(n,i,num)