# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    coins = [1,2,5,10,20,50,100,200]
    num_of_ways = 0
    for i in range(len(coins),0,-1):
        for amount in coins[i]:
            if pence%coins == 0:
                num_of_ways += 1
            else:
                
def decompose(pence):
    coins = [1,2,5,10,20,50,100,200]
    for i in range(len(coins)):
        if pence>coins[i]:
            num_of_ways += 1
            if pence>coins[i-1]:
                num_of_ways += 1
    return num_of_ways