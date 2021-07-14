# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    if num == 0:
        return 0
    x = 1
    for j in range(i):
        fx = x**n - num
        if n > 2:
            fdx = x**(n-1)*n
        else:
            fdx = x*2
        x -= fx/fdx
    return round(x,3)

def nroot_complex(n, i, num):
    if num>=0:
        return nroot(n, i, num)
    if n%2 == 0:
        return nroot(n, i, -num) * 1j
    else:
        return -nroot(n, i, -num)