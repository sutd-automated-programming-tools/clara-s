# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 1
    for a in range(1, pence+1, 1):
            for b in range(1, pence+1-a, 2):
                for c in range(1, pence+1-a-b, 5):
                    for d in range(1, pence+1-a-b-c, 10):
                        for e in range(1, pence+1-a-b-c-d, 20):
                            for f in range(1, pence+1-a-b-c-d-e, 50):
                                for g in range(1, pence+1-a-b-c-d-e-f, 100):
                                    for h in range(1, pence+1-a-b-c-d-e-f-g, 200):
                                        count += 1
    return count