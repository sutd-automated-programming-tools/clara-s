# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 0
    x1 = 1
    x2 = 2
    x3 = 5
    x4 = 10
    x5 = 20
    x6 = 50
    x7 = 100
    for x1 in range(pence+1):
        for x2 in range(pence+1-x1):
            for x3 in range(pence+1-3*x1):
                for x4 in range(pence+1-8*x1):
                    for x5 in range(pence+1-18*x1):
                        for x6 in range(pence+1-38*x1):
                            for x7 in range(pence+1-88*x1):
                                count += 1