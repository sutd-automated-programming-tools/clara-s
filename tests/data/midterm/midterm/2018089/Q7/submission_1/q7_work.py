# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 1:
        result = 1
        return result
    num_combi = 0
    for a in range (pence-1):
        num_combi +=1
    return num_combi
print (decompose(1))