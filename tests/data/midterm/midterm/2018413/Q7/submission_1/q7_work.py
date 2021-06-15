# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 0:
        return 0
    coin_value = [1, 2, 5, 10,20,50,100,200]
    
    def helper(amt, coin_value):
        for n in range(0,8):
            if amt==1:
                return 0
            else:
                return helper(amt,coin_value[n+1]) + helper (amt-coin_value[n], coin_value[n])  #checks the next coin value in list
            return helper(pence, coin_value) #goes through loop for every coin value