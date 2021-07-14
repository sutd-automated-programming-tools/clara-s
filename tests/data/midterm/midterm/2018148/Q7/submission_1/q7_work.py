# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence == 1:
        return 1
    else:
        coin_list = [1,2,5,10,20,50,100,200]
        for penny in coin_list[::-1]:
            if pence <= penny: