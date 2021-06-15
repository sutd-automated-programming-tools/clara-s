# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    
    if pence==0: 
        return 0 
    def helper(amt, coin_value): 
        if amt< coin_value:
            return 0 
        elif amt == coin_value:
            return 1 
        else: 
            return helper(amt, coin_value*2) + helper (amt-coin_value ,coin_value)
        
    return helper (pence,1) 
