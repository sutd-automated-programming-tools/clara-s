def decompose(pence):
    ways = 1 # using just 1p, there is only one combination
    if pence >= 200:
        different_coins = [2, 5, 10, 20, 50, 100, 200]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 200 and pence >= 100:
        different_coins = [2, 5, 10, 20, 50, 100]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 100 and pence >= 50:
        different_coins = [2, 5, 10, 20, 50]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 50 and pence >= 20:
        different_coins = [2, 5, 10, 20]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 20 and pence >= 10:
        different_coins = [2, 5, 10]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 10 and pence >= 5:
        different_coins = [2, 5]
        for i in different_coins:
            num = pence // i
            for i in range(num):
                ways += 1
    elif pence < 5 and pence >= 2:
        different_coins = [2]
        num = pence // 2
        for i in range(num):
            ways += 1
    elif pence < 2 and pence >= 1:
        ways = 1
    return ways

print(decompose(7))