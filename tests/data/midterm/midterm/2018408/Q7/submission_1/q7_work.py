# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    index = 1
    if pence % 2 == 0:
        index += 2
    if pence % 5 == 0:
        index += 1
    return index