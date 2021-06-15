def decompose(pence):
    count = 0
    if pence == 1:
        return 1
    if pence == 2:
        return 2
    coins = [200,100,50,20,10,5,2,1]
    
    while pence!= 0:  
        i = 0
        if pence >= coins[i]:
            pence -= coin
            lst.append[coin]
        else:
            i += 1
    count += 1
    for coin in lst:
        count+= decompose(coin)
        
print(decompose(5))
