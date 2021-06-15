# MID-TERM EXAM: QUESTION 7

list_currency_pence = [1,2,5,10,20,50,100,200]

def decompose(pence):
    
    minimal_currency_pence = []
    for i in range(len(list_currency_pence)):
        if pence >= list_currency_pence[i]:
            minimal_currency_pence.append(list_currency_pence[i])
    
    for k in range(len(minimal_currency_pence)):
        counter = 0
        if type(pence/minimal_currency_pence[k]) == int:
            counter = counter + 1
    return counter
            