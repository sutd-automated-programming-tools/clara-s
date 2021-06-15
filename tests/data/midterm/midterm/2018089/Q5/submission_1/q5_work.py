# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):#to determine non-negative num
    x = (num**(1/n))
    return (round(x,3))

def nroot_complex(n,t,num): #to determine root of negative num
    if num > 0:
        return nroot(n, t, num)
    elif num < 0 and n%2 == 0:
        return (n)*(1j)
    elif num < 0 and n%2 == 1:
        num = num*(-1)
        output = (nroot(n, t, num))*(-1) 
        return output
print (nroot_complex(2, 5, -4)) 
'''
def nroot(n, t, num): #to determine non-negative num


def nroot_complex(n, t, num): 
    if num > 0:
        return nroot(n, t, num)
    elif num < 0 and n%2 == 0:
        return str(n)+('j')
    elif num < 0 and n%2 == 1:
        num = num*(-1)
        output = (nroot(n, t, num))*(-1) 
        return output
print (nroot_complex(3, 5, -8)) 
'''