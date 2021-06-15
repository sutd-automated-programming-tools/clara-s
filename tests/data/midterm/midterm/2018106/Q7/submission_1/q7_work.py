# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence==1:
        ways=1
    elif pence<100:
        ways=pence-1
    
    return ways
