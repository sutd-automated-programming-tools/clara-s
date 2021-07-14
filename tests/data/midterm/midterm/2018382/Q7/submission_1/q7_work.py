# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    types = [1,2,5,10,20,50,100,200]
    opt = [1,2]
    two =pence//2
    one =pence%2  #APPROACH to find how many 2 and 1p make up pence, and find permutations of rest that can replace
    
    five= two
    
    counter = 0
    #for i in range(1,pence+1):
       # for a in types:
        #    for b in types:
             #   if a+b==pence:
                 #   counter += 1
    return counter