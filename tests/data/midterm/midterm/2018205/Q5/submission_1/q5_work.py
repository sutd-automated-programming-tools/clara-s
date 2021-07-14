# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):                     #eg (2,5,2)
    fx = 1**n - num                     #sub x =1 for initial state
    ffx = n*(1**(n-1))    
    x= 1 
                               
    for i in range(1,t):               
        fx = i**n - num                 # i=1, f(x1)
        ffx = n*(i**(n-1))                 # ff(x1) 
        newx = x - ((fx)/(ffx))            # where x starts from 1
        x = newx                           #replace x with newx for next loop
        
    return x

def nroot_complex(n,t,num):
    pass

print(nroot(2,5,2))