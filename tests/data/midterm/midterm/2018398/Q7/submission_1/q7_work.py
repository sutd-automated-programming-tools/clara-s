# MID-TERM EXAM: QUESTION 7

def decompose(pence, x= 8):
    if pence == 0:
        return 0
    if pence == 1:
        return 1
    ans = sum([decompose(pence-m, x-1) for m in range(pence+1)])
    if ans >50000000:
        break
    else:
        return ans
    