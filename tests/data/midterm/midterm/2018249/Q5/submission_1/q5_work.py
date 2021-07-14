# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    pass

def nroot_complex(n,t,num):
    pass
def nroot(n, i, num):
    x0 = 1
    for k in range(i):
        x1 = x0 - (x0**n - num)/(n*(x0)**(n - 1))
        x0 = x1
    return round(x0, 3)

def nroot_complex(n, i, num):
    if num > 0:
        ans = nroot(n, i, num)
        return ans
    else:
        if n%2 == 0:
            num1 = -1*num
            ans = nroot(n, i, num1)
            return (str(ans) + 'j')
        elif n%2 != 0:
            num1 = -1*num
            ans = nroot(n, i, num1)
            return -1*ans