# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ls = [1, 2, 5, 10, 20, 50, 100, 200]
    ls2 = reversed([a for a in ls if a <= pence])

    left = pence
    ls3 = []
    for i in ls2:
        if pence > i:
            pence -= i
            ls3.append(i)
    s = 0
    for i in ls3:
        if i == 1:
            s += 1
        if i == 2:
            s += 2
        if i == 5:
            s += 4
    return i