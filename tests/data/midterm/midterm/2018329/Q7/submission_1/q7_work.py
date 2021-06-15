# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    p1 = 1
    p2 = 2
    p5 = 5
    p10 = 10
    p20 = 20
    p50 = 50
    p100 = 100
    p200 = 200
    
    if pence == 1:
        return (1)
    if pence == 2:
        return (3)
    if pence == 5:
        return (decompose(2))