# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    count = 0
    x = 1
    while count < t:
        if n == 2:
            span = (x**2 - num)/(2 * x)
            
        elif n == 3:
            span = (x**3 - num)/(3 * x**2)
        x -= span
        count += 1
    
    x = round(x, 3)
    return x

def nroot_complex(n,t,num):
    if num >0:
        return nroot(n, t, num)
    else:
        if n%2 == 0:
            ans = nroot(n, t, abs(num))
            return ans * 1j
        
        if n%2 == 1:
            ans = nroot(n, t, abs(num))
            return ans*(-1)
        