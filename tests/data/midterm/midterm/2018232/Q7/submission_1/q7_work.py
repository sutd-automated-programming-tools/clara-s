# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    liss = [1, 2, 5, 10, 20, 50, 100, 200]
    count  = []
    num = 0
    for i in range(pence):
        for j in liss:
            count.append(i*j)
    for n in count:
        if n == pence:
            num += 1
    return num