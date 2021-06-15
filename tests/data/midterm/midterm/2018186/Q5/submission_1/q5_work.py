# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    return round(num**(1/n), 3)


def nroot_complex(n,t,num):
    cal = nroot(n, t, abs(num))
    if n % 3==0:
        return cal*-1
    elif n%2 == 0:
        return cal*1j
    else:
        return cal