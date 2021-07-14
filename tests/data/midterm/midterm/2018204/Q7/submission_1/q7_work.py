# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    x1 = 1
    x2 = 2
    x3 = 5
    x4 = 10
    x5 = 20
    x6 = 50
    x7 = 100
    x8 = 200
    n = pence
    count = 0
    for x in range(n//x8):
        if n > x8*n:
            n = n - x*x8
            if n == 0:
                count = count + 1
        for x in range(n//x7):
            if n > x7*n:
                n = n - x*x7
                if n == 0:
                    count = count + 1
            for x in range(n//x6):
                if n > x6*n:
                    n = n - x*x6
                    if n == 0:
                        count = count + 1
                for x in range(n//x5):
                    if n > x5*n:
                        n = n - x*x5
                        if n == 0:
                            count = count + 1
                    for x in range(n//x4):
                        if n > x4*n:
                            n = n - x*x4
                            if n == 0:
                                count = count + 1
                        for x in range(n//x3):
                            if n > x3*n:
                                n = n - x*x3
                                if n == 0:
                                    count = count + 1
                            for x in range(n//x2):
                                if n > x2*n:
                                    n = n - x*x2
                                    if n == 0:
                                        count = count + 1
                                for x in range(n//x1):
                                    if n > x1*n:
                                        n = n - x*x1
                                        if n == 0:
                                            count = count + 1
    return count