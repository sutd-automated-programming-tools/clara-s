# MID-TERM EXAM: QUESTION 7

#if pence can be made up of n times 20 p it can also be made up of x times 10 of 2p
# 2 pounds can be made from 8 diff combi f the other coins
# 1 pound can be made up of 7 diff combi of the other coins
# 50 p = 4 combi
#20 p = 4 combi
#10 p = 3 combi
# start finding from 2 pounds down to 10 p




def decompose(pence):
    count = 0
    if pence == 1:
        return 1
    elif pence // 200 >= 1:
        remainder = pence % 200
        quotient = pence // 200
        qtimes = 8 * quotient
        count += qtimes
        if remainder // 100 >= 1:
            r = remainder % 100
            q = remainder // 100
            qtimes1 = 7 * q
            count += qtimes1
            if r // 50 >= 1:
                r2 = r % 50
                q2 = 
        
        
    
    pence > 200:
        remainder = pence % 200
        quotient = pence // 200
        remainder
    