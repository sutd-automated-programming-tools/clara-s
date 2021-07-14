# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x = 1
    f_x = x**n - num
    f_x1 = n*x
    for a in range(i):
        f_x = x**n - num
        f_x1 = n*x
        x = x - f_x/f_x1
    return round(x,3)

def nroot_complex(n,i,num):
    if num < 0:
        num = abs(num)
        ans = nroot(n,i,num) * 1j
    else:
        ans = nroot(n,i,num)   
    return ans