# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ways = 0
    if pence == 1:
        return 1
    '''more than 1 pence'''
    while pence != 0:
        ways = 1
        '''2p'''
        if pence >= 200:
            if pence%2 == 0:
                ways += 1
            else:
                quotient = pence//2
                pence -= quotient*2
        elif pence >= 100:
            if pence == 0:
                pass
            quotient = pence//2
    coin_ls = [1,2,5,10,100,200]
    for x in range(len(coin_ls)):
        for i in range(pence, -1, -coin_ls[x]):
            pence = pence-coin_ls[x]