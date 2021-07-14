# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for i in range(i):
        x = x - (x**n - num)/(n*x**(n-1))
    return round(x, 3)

def nroot_complex(n, i, num):
    if n%2 == 0:
        answer = nroot(n, i, abs(num))
        return (answer)*1j
    elif n%2 == 1:
        return -nroot(n, i, abs(num))