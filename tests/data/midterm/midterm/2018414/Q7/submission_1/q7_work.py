# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    dic = {'1p':1,'2p':2, '5p':5, '10p':10, '20p':20, '50p':50, '1pound':100, '2pound':200}
    combinations = 0
    for i in range(pence):
        for k,v in dic.items():
            #find combination
            seq = range(pence,-1,-v)
            combinations += len(seq)-1
    return combinations