# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    leftover = pence
    count = 0
    while leftover > 0:
        if leftover >= 200:
            leftover -= 200
            count += 160
        elif leftover >= 100:
            leftover -=100
            count += 80
        elif leftover >= 50:
            leftover -= 50
            count += 40
        elif leftover >= 20:
            leftover -= 20
            count += 16
        elif leftover >= 10:
            leftover -=10
            count += 8
        elif leftover >= 5:
            leftover -=5
            count += 4
        elif leftover >= 2:
            leftover -=2
            count += 2
        elif leftover >= 1:
            leftover -=1
            count += 1
    return count