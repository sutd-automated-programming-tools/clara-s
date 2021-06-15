# MID-TERM EXAM: QUESTION 5
import math
import sympy

def nroot(n,t,num):
    x = sympy.symbols('x')
    x_i=x**n-num
    for iteration in range(t):
        x_diff=sympy.diff(x_i,x)
        x_i += - x/x_diff
    return x_i
        

def nroot_complex(n,t,num):
    pass