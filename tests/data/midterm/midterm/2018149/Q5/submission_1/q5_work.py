# MID-TERM EXAM: QUESTION 5


from sympy import diff, Symbol

def nroot(n,i,num):
    x = Symbol('x')
    fx = x^n - num
    count = 1
    dx = diff(fx, x, count)
    
    for count in range(1,i+1):
        
        dx = diff(fx, x, count)
        x = x - fx/dx
        fx = dx
        ans = x
        
    return ans.subs({x:num})
                    
print(nroot(2,5,2))

def nroot_complex(n,i,num):
    ans = nroot(n,i,num)
    if num > 0:
        return ans
    if num < 0 and num%2 == 0:
        return ans.imag()
    if num < 0 and num%2 != 0:
        return (-1) * abs(ans.real())