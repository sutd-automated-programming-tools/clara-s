# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    if i == 0:
        return 1
    f = lambda x: x**n - num
    f_p = lambda x: n*x**(n-1)
    x_i_1 = nroot(n, i-1, num)
    value = x_i_1 - f(x_i_1)/f_p(x_i_1)
    return value

def nroot_complex(n, i, num):
    if num < 0:
        if n%2 == 0:
            return round(nroot(n,i,-num),3)*1j
        else:
            return round(-1*nroot(n,i,-num),3)
    elif num >= 0:
        return round(nroot(n,i,num),3)