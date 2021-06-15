# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    change = [1, 2, 5, 10, 20, 50, 100, 200]
    p = pence 
    amt = (p+1)*[0]  
    amt[0] = 1
    for coin in change:
        for j in range(coin, p+1):
            amt[j] += amt[j - coin]
    return amt[p]