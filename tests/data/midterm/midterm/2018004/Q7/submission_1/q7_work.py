# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ways = 0
    p = pence + 1
    for i in range(0,p):
        for j in range(0,p,2):
            for k in range(0, p, 5):
                for l in range(0,p,10):
                    for m in range(0,p,20):
                        for n in range(0,p,50):
                            for o in range(0,p,100):
                                for x in range(0,p,100):
                                    if i + j + k + l + m + n + o + x == pence:
                                        ways += 1
    return ways