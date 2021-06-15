# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = num ** (1/n)

    return x

def nroot_complex(n,t,num):
    n_rt = nroot(n,t,num)
    if num % 2 != 0:
        return n_rt
    else