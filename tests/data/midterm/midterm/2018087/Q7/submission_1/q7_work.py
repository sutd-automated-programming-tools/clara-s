# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    numways = 0
    pc = pence + 1
    for a in range(0, pc):
        for b in range(0, pc, 2):
            for c in range(0, pc, 5):
                for d in range(0, pc, 10):
                    for e in range(0, pc, 20):
                        for f in range(0, pc, 50):
                            for g in range(0, pc, 100):
                                for h in range(0, pc, 100):
                                    if a+b+c+d+e+f+g+h == pence:
                                        numways = numways+1
    return numways