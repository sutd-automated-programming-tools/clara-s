# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    A = {1 : 200
         2 : 100
         3 : 50
         4 : 20
         5 : 10
         6 : 5
         7 : 2
         8 : 1}
    count = 0
    #pence is the sum of all combinations
    #2 pence can be made with 2 1pence
    #5 pence can be made with 5 1pence
    #5%2 = 1 5//2 = 2
    #5//2 = 2 2pence can be futher borken down into 1 pence
    #create a dictionary with values to each coin and the number of combinations it can be made from with coins smaller than it by the method of remainders 
    