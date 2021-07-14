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
    ls = [x1,x2,x3,x4,x5,x6,x7,x8]
    a = 0
    for i1 in range(len(ls)):
        if ls[i1] == pence:
            a += 1
        for i2 in range(len(ls)):
            if ls[i1] + ls[i2] == pence:
                a += 1
            for i3 in range(len(ls)):
                if ls[i1] + ls[i2] + ls[i3] == pence:
                    a += 1
                for i4 in range(len(ls)):
                    if ls[i1] + ls[i2] + ls[i3] + ls[i4] == pence:
                        a += 1
                    for i5 in range(len(ls)):
                        if ls[i1] + ls[i2] + ls[i3] + ls[i4] + ls[i5] == pence:
                            a += 1
                        for i6 in range(len(ls)):
                            if ls[i1] + ls[i2] + ls[i3] + ls[i4] + ls[i5] + ls[i6] == pence:
                                a += 1
                            for i7 in range(len(ls)):
                                if ls[i1] + ls[i2] + ls[i3] + ls[i4] + ls[i5] + ls[i6] + ls[i7] == pence:
                                    a += 1
                                for i8 in range(len(ls)):
                                    if ls[i1] + ls[i2] + ls[i3] + ls[i4] + ls[i5] + ls[i6] + ls[i7] + ls[i8] == pence:
                                        a += 1
    return a