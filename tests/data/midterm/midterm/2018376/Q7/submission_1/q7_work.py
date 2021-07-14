# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence >= 200:
        twopounds = pence/200
        rem_pence = pence%200
    if rem_pence >= 100:
        pounds = rem_pence/100
        rem_pence = rem_pence%100
    if rem_pounce >= 50:
        fiftyp = rem_pence/50
        rem_pence = rem_pence%50
    if rem_pounce >= 20:
        twentyp = rem_pence/20
        rem_pence = rem_pence%20
    if rem_pounce >= 10:
        tenp = rem_pence/10
        rem_pence = rem_pence%10
    if rem_pounce >= 5:
        fivep = rem_pence/5
        rem_pence = rem_pence%5
    if rem_pounce >= 2:
        twop = rem_pence/2
        rem_pence = rem_pence%2
    if rem_pounce >= 1:
        onep = rem_pence/1
    count = 1
    
    for coin in twop:
        count = count*2
    for coin in fivep:
        count = count*3*5
    for coin in tenp:
        count = count*2*4*6
        
    
    
    return count
