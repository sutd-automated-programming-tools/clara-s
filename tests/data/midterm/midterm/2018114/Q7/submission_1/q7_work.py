# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    a = 1 #only method for pence in 1p
    for pence%2 == 0 and pence<5:
        b = 1 #only method for pence in 2p
        c = pence/2 #method for pence in 2p and 1p
        return a+b+c
    for pence%2 != 0 and pence<5:
        e = (pence-1)/2 #method for pence in 2p and 1p
        return e+2
    for pence%2 == 0 and pence%5 != 0 and pence<10:
        return pence/2+2
    for pence%5 == 0 and pence<10:
        pence = (pence-1)/2+2
        
    pass