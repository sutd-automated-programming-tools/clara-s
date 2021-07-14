# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    import random
    #find the number of ways of money to add up to the following value
    uk_money = [1,2,5,10,20,50,100,200]
    count = 0
    counter = 0
    while counter < 8**8: #8**8 is the max aount of combination
        a = uk_money[random.randint(0,8)]
        b = uk_money[random.randint(0,8)]
        c = uk_money[random.randint(0,8)]
        d = uk_money[random.randint(0,8)]
        e = uk_money[random.randint(0,8)]
        f = uk_money[random.randint(0,8)]
        g = uk_money[random.randint(0,8)]
        h = uk_money[random.randint(0,8)]
        overall = a + b + c + d + e + f + g + h
        if overall == pence:
            count += 1
        counter += 1
    return count