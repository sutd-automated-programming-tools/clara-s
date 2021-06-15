# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    val = 1
    for x in range(i):
        val = val - (val**n - num)/(n*val**(n-1))
    return round(val,3)

def nroot_complex(n, i, num):
    if n % 2 == 0:
        return nroot(n, i, -num)*1j
    if n % 2 == 1:
        return -nroot(n, i, -num)