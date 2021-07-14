# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 0
    pence1 = [1,2,5,10,20,50]
    pound = [1,2]
    if pence >= 100:
        pounds = pence//100
        rem_pence = pence%100
        for n in range(len(pence1)):
            if rem_pence % pence1[n] == 0:
                count += 1
    
        
    return count