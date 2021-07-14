# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    a = 1
    b = 2
    c = 5
    d = 10
    e = 20
    f = 50
    g = 100
    h = 200
    z = 1
    for i in range(pence):
        for j in range(pence):
            for k in range(pence):
                for l in range(pence):
                    for m in range(pence):
                        for n in range(pence):
                            for o in range(pence):
                                for p in range(pence):
                                    if i * a + j * b + k * c + l * d + m * e + n * f + o * g + p * h == pence:
                                        z += 1
    return z