# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    counter = 0
    for coin_val in [1,2,5,10,20,50,100,200]:
        pence_left = pence
        if coin_val>pence_left:
            break
        while coin_val<=pence_left:
            pence_left -= coin_val
        counter+=1
        if pence_left == 0:
            pass
        elif pence_left > 1:
            counter+=decompose(pence_left)
        elif pence_left == 1:
            counter+=1      
    return counter
        