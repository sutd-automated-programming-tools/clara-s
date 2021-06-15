def nroot(n, i, num):
    z = 1
    x = (num)**(1/n)
    f = (x**n) - num
    f1 = n*x
    x1 = x - (f/f1)
    for z in range(i):
        value = x1
    return round(value, 3)


def nroot_complex(n, i, num):
    if num >= 0:
        output = nroot(n, i, num)
        return output
    if num < 0:
        num = -num
        output = nroot(n,i,num)
        return (output, "j")
    if num < 0 and n%2 != 0:
        num = -num
        output = -nroot(n, j, num)
        return output
