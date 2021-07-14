
def decompose(pence):
    #recursion
    validlst = [1,2,5,10,20,50,100,200]
    count = 0
    pence = int(pence)
    if pence == 1:
        count += 1
    if pence == 2:
        count += 1
    if pence == 5:
        count += 4
    else:
        for coin in validlst:
            if pence % coin == 0:
                count += 1
            else:
                count += decompose(pence%coin)
    return count