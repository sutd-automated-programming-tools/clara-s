def decompose(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    count = 0
    i = 0
    x = n
    while True:
        while x!=0:
            x = x%coins[i]
            if x < coins[i]:
                break
        i += 1
        if x == 0:
            count+=1
            x = n
            if i == 7:
                break