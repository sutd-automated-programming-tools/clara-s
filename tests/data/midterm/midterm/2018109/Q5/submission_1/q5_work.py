# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    if num < 0:
        return
    return round(num ** (1/n),3)
def nroot_complex(n,i,num):
    if num >0:
        return nroot(n,i,num) 
    magnum = num * -1
    if n % 2 == 0:        
        return int((nroot(n,i,magnum))) * 1j
    elif n % 2 ==1:
        return -1 * nroot(n,i,magnum)