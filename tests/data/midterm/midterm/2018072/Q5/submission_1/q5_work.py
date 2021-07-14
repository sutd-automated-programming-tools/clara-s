# MID-TERM EXAM: QUESTION 5


def nroot(n,t,num):
    x = []
    for i in range(t):
        root = num**(1/n)
        x.append(root)
        x[i] = x[i-1] - (((x[i-1]**n)-num)/(x[i-1]*n))
        newroot = round(x[-1], 3)
    return newroot


def nroot_complex(n,t,num):
    num = abs(num)
    newroot = nroot(n,t,num)
    if n%2 == 0:
        newc = newroot*1j
        return newc
    elif n%2 != 0:
        newp = -newroot
        return newp
    