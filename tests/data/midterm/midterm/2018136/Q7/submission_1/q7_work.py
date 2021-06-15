# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    dic = {1,2,5,10,20,50,100,200}
    for a1 in range(pence,-1,-1):
        #print(a1)
        pass
    for a2 in range(pence,-1,-2):
        pass
        #print(a2)
    a3 = range(pence,-1,-5)
    a4 = range(pence,-1,-10)
    a5 = range(pence,-1,-20)
    a6 = range(pence,-1,-50)
    a7 = range(pence,-1,-100)
    a8 = range(pence,-1,-200)
    return a1+a2+a3+a4+a5+a6+a7+a8

#code should take in pence amount and compute the number of permutation possible based on given values (the eight coins)