# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    c1 = 1
    c2 = 2
    c3 = 5
    c4 = 10
    c5 = 20
    c6 = 50
    c7 = 100
    c8 = 200
    solution = 0
    for c1i in range(1, pence+1):
        for c2i in range(2, pence+1, 2):
            for c3i in range(5, pence+1, 5):
                for c4i in range(10, pence+1, 10):
                    for c5i in range(20, pence+1, 20):
                        for c6i in range(50, pence+1, 50):
                            for c7i in range(100, pence+1, 100):
                                if (c1+c2+c3+c4+c5+c6+c7+c8) == pence:
                                    solution += 1
                                    c7 = 100
                                    break
                                for c8i in range(200, pence+1, 200):
                                    c8 = c8i
                                    if (c1+c2+c3+c4+c5+c6+c7+c8) == pence:
                                        solution += 1
                                        c8 = 200
                                        break