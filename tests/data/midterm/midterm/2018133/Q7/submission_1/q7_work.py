# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence <= 1:
        decompose = 1
    elif pence <= 2:
        decompose = 2
    elif pence <= 5:
        decompose = pence%2*2
    elif pence <= 10:
        decompose = pence%5*4 + (pence - pence%5*5)%2*2
    elif pence <= 20:
        decompose = pence%10*