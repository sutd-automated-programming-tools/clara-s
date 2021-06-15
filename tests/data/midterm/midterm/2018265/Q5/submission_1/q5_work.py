# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
    if num > 0:
        x = 1
        num = x**n
        func = x**n - num 
        deriv = (n-1)*x**n
        diff = x1 - x 
        while -0.01 < diff < 0.01:
            x1 = x - func/deriv 
            x = x1 
            
        return round(x1, 3)

def nroot_complex(n, i, num):
    if num < 0: 
        if n % 2 == 0:
            ans1 = '{}j'.format(nroot(n))
            return ans1
        else:
            ans2 = -1 * nroot(n) 
            return ans2