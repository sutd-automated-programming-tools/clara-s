# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    root = num**(1/n)
    return round(root,3)


def nroot_complex(n,t,num):
    if num < 0 and n % 2 == 0:
        newnum = num / (-1)
        root = newnum**(1/n)
        ans = root * 1j
    elif num < 0 and n % 2 != 0:
        newnum = num / (-1)
        root = nroot(n,t,newnum)       
        ans = -1 * root 
    return ans
    