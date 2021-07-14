# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    num_0 = 1
    for i in range(1,t+1):
        num_0 = num_0 - (num_0**n-num)/((n)*(num_0)**(n-1)) 
    return round(num_0,3)
    
def nroot_complex(n,t,num):
    if num >= 0:
        value = nroot(n,t,num)
        return value
    elif n%2 == 0:
        num = abs(num)
        value2 = nroot(n,t,num)
        value2 = value2*1j
        return value2
    else:
        num = abs(num)
        value2 = nroot(n,t,num)
        value2 = -value2
        return value2
    