# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for e in range(i):
        x = x - (((x**n)-num)/(n*(x**(n-1))))
    return round(x,3)

def nroot_complex(n,t,num):
    if num <0 and n%2 !=0:
        return nroot(n, t, num)
    else:
        num = num * -1
        ans = nroot(n, t, num) * 1j
        return ans