# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x = num
    for i in range(t):
        
        f = x**n - num
        f_dash = n*x**n-1
        x = x - (f/f_dash)
        

        
        
    return round(x,3)
    pass

def nroot_complex(n,t,num):
    if num>0:
        return nroot(n,t,num)
    elif num<0 and n%2==0:
        val = nroot(n,t,-num)
        return val*1j
    elif num <0 and n%2!=0:
        val= nroot(n,t,-num)
        return float(val)
    
    
print(nroot(2,5,4)
    