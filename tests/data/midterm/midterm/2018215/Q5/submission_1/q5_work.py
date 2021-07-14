# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x1 = 1
    for i in range(1, t + 1):
        fx = (x1 ** n) - num
        fpx = n * (x1**(n - 1))
        x = x1 - ((fx) / fpx)
        x1 = x
    return round(x1, 3)

def nroot_complex(n,t,num):
    if num > 0:
        return nroot(n, t, num)
    elif num < 0 and n % 2 == 0:
        positive = num / -1
        real = nroot(n, t, positive)
        result = real * 1j
        return result
    elif num < 0 and n % 2 == 1:
        positive = num / -1
        real = nroot(n, t, positive)
        result = real * -1
        return result