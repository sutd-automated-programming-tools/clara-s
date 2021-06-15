# MID-TERM EXAM: QUESTION 7

def decompose(pence,pences = [1,2,5,10,20,50,100,200]):
    if pence == 0:
        return 1
    elif pence < 0 or len(pences) == 0:
        return 0
    else:
        ans = sum(decompose(new_pence, pences[:-1]) for new_pence in range(pence,-1,-pences[-1]))
    return ans
    pass