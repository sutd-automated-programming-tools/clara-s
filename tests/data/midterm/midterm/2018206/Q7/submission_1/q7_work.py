# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    x1= 1
    x2= 2
    x5 = 5
    x10 = 10
    x20= 20
    x50 = 50
    x100 = 100
    x200 = 200
    
    
    count = 1
    for i in range(pence):
        if pence == x1:
            return count
        else:
            for i in range(pence/x2):
                if x1+i*x2 == pence:
                    count += 1
                    
    return count