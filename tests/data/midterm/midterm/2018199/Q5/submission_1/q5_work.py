# MID-TERM EXAM: QUESTION 5

def f(p,x,n):
    result = (x**p)-n
    return result
def fp(p,x):
    result = p*(x**(p-1))
    return result

def nroot(n,t,num):
    x = 1
    for i in range(t+1):
        result = x - (f(n,x,num)/fp(n,x))
        x = result
    result = round(result,3)
    return result

def nroot_complex(n,t,num):
    if num<0 and n%2 == 0:
        return nroot(n,t,(-num))*1j
    else:
        return nroot(n,t,num)

print(nroot_complex(3,5,-8))