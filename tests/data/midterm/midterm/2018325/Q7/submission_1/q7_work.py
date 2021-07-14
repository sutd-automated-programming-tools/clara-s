# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    poss = 0
    
    ichi = 1
    ni = 2
    go = ni + ni +ichi -1
    juu = go +go -1
    nijuu = juu+ juu - 1
    gojuu = (nijuu + nijuu + juu) -1
    hyaku = gojuu + gojuu -1
    nibyaku = hyaku + hyaku -1
    

    if pence % 2 == 0: #even pence
        x = pence//2
        poss = x*2 -x
    
        
    #let pence = multiples of 1,2
    #eg pence = 5 = 2*2*1
    #for every common multiple -1
    #therefore decompose(5) = 2+2+1 -1 = 4
    #decompose(10) = 2+2+2+2+2 -5
    
    
    return poss