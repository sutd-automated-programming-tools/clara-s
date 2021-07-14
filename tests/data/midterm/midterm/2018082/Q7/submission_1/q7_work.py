# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 1:
        return 1
    elif pence == 2:
        return 1 + pence(1)
    elif pence == 5:
        return pence(2) + pence(1) + 1
    elif pence == 10:
        return pence(1) + pence(2) + pence(5) +1
    elif pence == 20:
        return pence(1) + pence(2) + pence(5) + pence(10) + 1
    elif pence == 50:
        return pence(1) + pence(2) + pence(5) + pence(10) + pence(20) + 1
    elif pence == 100:
        return pence(1) + pence(2) + pence(5) + pence(10) + pence(20) + pence(100) + 1
    else:
        return pence(1) + pence(2) + pence(5) + pence(10) + pence(20) + pence(100) + pence(200) +1