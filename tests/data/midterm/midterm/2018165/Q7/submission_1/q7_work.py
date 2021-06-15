# MID-TERM EXAM: QUESTION 7

import math
def decompose(pence):
    coin = [200,100,50,20,10,5,2,1]
    method = range(pence,-1,-coin)
    for i in range(coin):
        if pence%i = 0:
            
            
            
    return max(method)
 #for i in list of coin, divide (pence)by i to determine if it is divisible by the largest denominator.
 #if (pence) is not divisible by i, move down the list sequentially(i+1) until (pence) is finally divisible == 0.
#find the maximum number of ways of denomination by using max(method) 


 ls = []  
     for i in coin:
        for j in coin:
            for k in coin:
                for l in coin:
                    for m in coin:
                        for n in coin:
                            for o in coin:
                                for p in coin:
           
                ls.append(i*j*k*l*m*n*o*p)
            return max ls[pence]