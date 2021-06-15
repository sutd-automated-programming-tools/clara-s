# MID-TERM EXAM: QUESTION 5

import math as m

def nroot(n,t,num):
    num = abs(num)
    ans = m.sqrt(num)
    return round(ans,3)
    
    
    
def nroot_complex(n,t,num):
    if num>=0:
        return nroot(n,t,num)
        
    elif num <0 and n%2==0:
        
        return nroot(n,t,num)*1j
                
    elif num<0 and n%2!=0:
        
        return int(nroot(n,t,num))