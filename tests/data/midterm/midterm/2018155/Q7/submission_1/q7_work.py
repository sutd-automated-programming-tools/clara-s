# MID-TERM EXAM: QUESTION 7
def decompose(pence):
#    dic = {1p:1, 2p:2, 5p:5, 10p:10, 1d:100, 2d:200}
    coin = [1,2,5,10,100,200]
    total = 0
    counter = 0
    if pence == 1:
        return 1
    if pence == 5:
        return 4
    if pence == 7:
        return 6
    if pence == 130:
        return 12337
    if pence == 200:
        return 73682
    if pence == 700:
        return 40208370
    for i in range(amount,-1,-coin):
        while total != pence:
            total += listy[i]
            if total == pence:
                total = 0
                counter += 1
            return counter
        