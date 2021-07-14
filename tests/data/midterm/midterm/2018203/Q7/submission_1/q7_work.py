# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    lst = [200, 100, 50, 20, 10, 5, 2, 1]
    solutions = 0
    if pence in range (1, 3):
        solutions += 1
    n = 0
    while n<len(lst):
        if pence < lst[n]:
            new_lst = lst[n+1:8]
        n += 1
    i = 0
    while i<len(new_lst):
        if pence%new_lst[i]!= 0:
            solutions += 1
            n += 1
        else:
            pence -= new_lst[i]
            decompose(pence)

            
# The above code may not be fully functional (due to a lack of time in running the script), but it is an attempt at a program to solve Question 7 recursively. I hope the following description of the intended functionality of the program is clear.
# Firstly, the code finds the greatest in the given denominations (200, 100, 50, 20, 10, 5, 2, 1) which is smaller than the value of the argument (pence), passed into the function.
# Then, the program tests if argument (pence) is divisible by any of the given denominations. If it is divisible by one of the denominations, one way of making up pence is by using multiples of that particular denomination.
# If pence is not divisible by the denomination, the denomination is deducted from pence to give a new value for the argument (pence), and then the program continues to try finding ways to form pence from the given denominations.
# This is repeated until finally, pence takes on the value of either 1 or 2, in which case, it can only be made up using the 1p denomination, hence there is only one way of forming the pence value.

            
        
        