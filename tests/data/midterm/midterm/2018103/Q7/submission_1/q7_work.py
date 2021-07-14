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
    number = 0
    for i in range(0,pence+1):
        for j in range(0,pence+1):
            for k in range(0,pence+1):
                for l in range(0,pence+1):
                    for m in range(0,pence+1):
                        for n in range(0,pence+1):
                            for o in range(0,pence+1):
                                for p in range(0,pence+1):
                                    if (p*a) + o*b + n*c + m*d + l*e + k*f + j*g + i*h == pence:
                                        number += 1
    return number