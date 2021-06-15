# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    final = []
    if pence == 1:
        return 1
    for i in range (pence-1):
        ans = pence - i
        final.append(ans)
        total = 0
    for i in final:
        total += 1
        
    return total
    