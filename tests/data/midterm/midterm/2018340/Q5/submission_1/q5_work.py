# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    x = 1
    for time in range(i):
        x = x - (x**n - num)/(n*x**(n-1))
    return round(x, 3)



def nroot_complex(n, i, num):
    if num > 0:
        return nroot(n, i, num)
    elif num == 0:
        return 0
    else:
        abs_num = abs(num)
        if n % 2 == 0: #even num
            output = nroot(n, i, abs_num)
            output = round(output, 3)
            output = str(output)
            return output+'j'
        else:# odd num
            output = nroot(n, i, abs_num)
            output = round(output, 3)
            return output*(-1)