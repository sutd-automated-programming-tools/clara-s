# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    result=1
    for i in range(0,t):
        result=result-((result**n-num)/(n*result))
    return round(result,3)
        
        
        
        
     

def nroot_complex(n,t,num):
    if num>0:
        return nroot(n,t,num)
    else:
        for i in range(0,t):
        result=result-((result**n-num)/(n*result))
            return result.format(imag)
        
        
    