# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ways = pence # if using 1p
    if pence % 2 == 0:
        ways += pence / 2 
        break
    if pence % 2 == 1:
        ways += (pence - 1) / 2 
        break
    if pence % 5 == 0:
        ways += pence / 5
        break
    if pence % 5 == 1:
        ways += (pence - 1) / 5
        break
    if pence % 5 == 2:
        ways += (pence - 2) / 5
        break
    if pence % 5 == 3:
        ways += (pence - 3) / 5
        break
    if pence % 5 == 4:
        ways += (pence - 4) / 5
        break
    if pence % 10 == 0:
        ways += (pence) / 10
    for i in range(10):
        if pence % 10 == i:
            ways += (pence - i) / 10
        break
    pass