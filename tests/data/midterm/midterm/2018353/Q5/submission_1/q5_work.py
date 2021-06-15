# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = 1
    for i in range(0,t):
        x -= (x**n - num)/(n*x**(n-1))
    return round(x,3)

def nroot_complex(n,t,num):
    answer = nroot(n,t,-num)
    if n%2 == 0:
        
        return answer*(1j)
    else:
        return (-1)*answer