# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    bases = [200,100,50,20,10,5,2,1]
    if pence == 2 :
        return 1
    if pence == 5 :
        return 3 
    
    s = 1
    for i in range(bases):
        s *= decompose(i+1) 
        
    return s
         