# MID-TERM EXAM: QUESTION 7
def decompose(pence):
    sol = 0
    for a in range(pence+1):
        for b in range(pence+1-a):
            for c in range(pence+1-a-b):
                for d in range(pence+1-a-b-c):
                    sol += 1
    return sol