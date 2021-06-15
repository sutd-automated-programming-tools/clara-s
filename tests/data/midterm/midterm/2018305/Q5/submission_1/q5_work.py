# MID-TERM EXAM: QUESTION 5

import numpy as np

def nroot(n,t,num):
    if( num < 0 ):
        return None
    
    else:
        x = (num) ** (1/n)
        ith = (i-1) - ( (i-1-num)/ np.diff(i-1-num) )
        return x 

        
        
def nroot_complex(n,t,num):
    if not( num < 0 ):
        return nroot(n, t, num)
    
    else:
        if( n % 2 == 0 ):
            bum = nroot(n, t, num) * j
            return bum 
        
        else:
            bumm = nroot_complex(n, t, num) + nroot(n, t, num)* j 
            return bumm