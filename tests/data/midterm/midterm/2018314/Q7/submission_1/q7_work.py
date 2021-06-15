# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ls = []
    for i in range(pence):
        for a in range(pence):
            for b in range(pence):
                for c in range(pence):
                    for d in range(pence):
                        for e in range(pence):
                            for f in range(pence):
                                for g in range(pence):
                                    if i*1 + a*2 + b*5 + c*10 + d*20 + e*50 + f*100 + g*200 == pence:
                                        ls.append('s')
                                    
    return len(ls) + 1