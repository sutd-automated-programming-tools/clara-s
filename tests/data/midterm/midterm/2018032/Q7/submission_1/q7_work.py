# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count=0
    for i in range(pence+1):
        for j in range(pence+1):
            for k in range(pence+1):
                for m in range(pence+1):
                    for n in range(pence+1):
                        for o in range(pence+1):
                            for p in range(pence+1):
                                for q in range(pence+1):
                                    if i+2*j+5*k+10*m+20*n+50*o+100*p+200*q==pence:
                                        count+=1
    return count