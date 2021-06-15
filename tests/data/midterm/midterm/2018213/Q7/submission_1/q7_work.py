# MID-TERM EXAM: QUESTION 7

def decompose(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if n ==2:
        return 2
    if n ==3:
        return 2
    if n ==5:
        return 4
    if n ==7:
        return 6
    else:
        
        n-1
        for m in range(n+1):
            
            return decompose(n-m)
    
print(decompose(8))