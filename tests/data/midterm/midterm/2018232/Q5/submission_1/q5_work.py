# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    if num ==0:
        x = 0
    x = 1
    count = 1
    if num<0:
        num = num*(-1)
    while count <= i:
        f = x**n - num
        f_prime = n*x**(n-1)
        x = x - f/f_prime
        count += 1
    if num<0:
        x = x*(-1)
    return round(x,3)


def nroot_complex(n, i, num):
    if n%2 == 0 and num<0:
        num = num*(-1)
        x = nroot(n, i, num)
        x = round(x,3)*1j

    else:
        x = nroot(n, i, num)
    
    return x