# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 0:
        return 0
    
    def helper(amt, coin_value):
        lst = [1,2,5,10,20,50,100,200]
        for i in lst:
            if amt < i:
                return 0
            elif amt == i:
                return 1
            else:
                return helper(amt, i*2) + helper(amt-i, i)
    return helper(pence, lst)