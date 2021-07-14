# MID-TERM EXAM: QUESTION 7
def decompose(pence):
    counter=0
    for a in range(1,pence):
        for b in range(1,pence):
            for c in range(1,pence):
                for d in range(1,pence):
                    for e in range(1,pence):
                        for f in range(1,pence):
                            for g in range(1,pence):
                                for h in range(1,pence):
                                    if 1*a + 2*b + 5*c +10*d +20*e +50*f + 100*g +200*h == pence:
                                        counter+=1
    return counter