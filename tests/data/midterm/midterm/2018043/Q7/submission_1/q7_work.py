# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 0
    for i1 in range(pence+1):
        for i2 in range(pence+1):
            for i3 in range(pence+1):
                for i4 in range(pence+1):
                    for i5 in range(pence+1):
                        for i6 in range(pence+1):
                            for i7 in range(pence+1):
                                if pence - (i1*200+ i2*100+ i3*50+ i4*20+ i5*10+ i6*5+i7*2) >=0:
                                    count+=1
    return count    