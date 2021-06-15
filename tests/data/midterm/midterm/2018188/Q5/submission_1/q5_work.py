# MID-TERM EXAM: QUESTION 5
from numpy import *
def nroot(n,t,num):
    x=1
    
    for i in range(n+1):
        x=x-(x**(n)-num)/(n*x**(n-1))
    return round(x,3)
        
    
    

def nroot_complex(n,t,num):
    if n%2!=0:
        return -1*nroot(n,t,num)*(1+j-np.real(1+j))
    else:
        return nroot(n,t,num)
        
    
       
    
    
    