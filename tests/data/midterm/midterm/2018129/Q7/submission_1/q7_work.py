def decompose(p):
    ways = 0
    wayy = {}
    coins = [1,2,5,10,20,50,100,200]
    for val in coins:
        if p % val == 0:
            ways += 1
#    if p % 2 == 0:
        
    for val in coins[::-1]:
#        print(val)
        if p > val:
            p -= val
            wayy[val] = 1
    wayy += 1
    for key in wayy:
        for val in coins:
            if val != key:
                if key % val == 0:
                    wayy += 1