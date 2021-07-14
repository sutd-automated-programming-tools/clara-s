# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    f2, f1, p50, p20, p10, p5, p2, p1 = 200, 100, 50, 20, 10, 5, 2, 1
    composition = {}
    combination = [0,0,0,0,0,0,0,0]
    
    if pence // f2 > 0:
        combination[0] = pence // f2
        pence = pence % f2
    if pence // f1 > 0:
        combination[1] = pence // f1
        pence = pence % f1
    if pence // p50 > 0:
        combination[2] = pence // p50
        pence = pence % p50
    if pence // p20 > 0:
        combination[3] = pence // p20
        pence = pence % p20
    if pence // p10 > 0:
        combination[4] = pence // p10
        pence = pence % p10
    