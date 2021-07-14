# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    counter = 1
    if pence%2 == 0:
        counter += pence/2
    if pence%5 == 0:
        counter +=4* pence/5
    if pence%10 == 0:
        counter += pence/10
    if pence%20 == 0:
        counter += pence/20
    if pence%50 == 0:
        counter += pence/50
    if pence%100 == 0:
        counter += pence/100
    if pence%200 == 0:
        counter += pence/200
    return counter
        
    #if pence% 1, 2, 5, 10, 20, 50, 100 or 200 > 0 add 1 way to counter