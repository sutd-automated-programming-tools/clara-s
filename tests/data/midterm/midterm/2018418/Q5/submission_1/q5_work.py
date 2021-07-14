# MID-TERM EXAM: QUESTION 5

def function_value(x,n,num):
    return x**n - num
def func_derv_value(x,n,num):
    return n*(x**(n-1))

def nroot(n,i,num):
    #n gives the nth rooth, i gives the no. of iteration, num provides the value
    value = 1
    for i in range(n+1):
        iteration = function_value(value,n,num)/func_derv_value(value,n,num)
        value -= iteration
    return round(value,3)

def nroot_complex(n,i,num):
    if num >= 0:
        return nroot(n,i,num)
    if num < 0 and n%2 == 0:
        return nroot(n,i,num)*1j.imag
    if num < 0 and n%2 != 0:
        return nroot(n,i,num)