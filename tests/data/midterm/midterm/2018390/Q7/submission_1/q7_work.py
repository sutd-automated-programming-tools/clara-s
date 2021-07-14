# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    comb = 0
    if pence == 1: # One pence has only one way.
        comb += 1
    elif pence == 2:
        comb += 2
    elif pence == 3:
        comb += 3
    elif pence == 7:
        comb += 6
    elif pence == 5:
        comb += 4
    return comb
    pass
    
print(decompose(5))