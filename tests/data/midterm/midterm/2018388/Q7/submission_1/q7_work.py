# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    counter = 0
    for one in range(pence, -1, -1):
        for two in range(pence, -1, -2):
            for five in range(pence, -1, -5):
                for ten in range(pence, -1, -10):
                    for twenty in range(pence, -1, -20):
                        for fifty in range(pence, -1, -50):
                            for pound1 in range(pence, -1, -100):
                                for pound2 in range(pence, -1, -200):
                                    if one + two + five + ten + twenty + fifty + 100*pound1 + 200*pound2 == pence:
                                        counter += 1
    return counter
