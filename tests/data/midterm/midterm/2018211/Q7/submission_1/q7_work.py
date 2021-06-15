# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    n = pence
    circulation = [1,2,5,10,20,50,100,200]
    lst = [1]*(n+1)
    for n in circulation[1:]:
        for i in range(len(lst[n:])):
            lst[i+n] += lst[i-n]
    return(lst[-1])