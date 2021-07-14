# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    p = pence
    count = 0
    if p == 1:
        return 1
    if p % 1 == 0:
        count += 1
    if p % 2 == 0:
        count += 1
    if (p%2)%1 == 0:
        count += 1
    if p % 5 == 0:
        count += 1
    if (p%5)%2 == 0:
        count += 1
    if (p%5)%1 == 0:
        count += 1
            
    return count