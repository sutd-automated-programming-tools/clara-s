# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    ways = 0
    if pence %1 == 0:
        ways += 1
    if pence %2 == 0:
        ways += (pence/2)
    if pence %2 != 0:
        ways += ((pence-1)/2)
    if pence %5 == 0:
        ways += ((pence)/5)
    if pence %5 != 0:
        ways += ((pence-(pence%5))/5)
            
    return ways

# MID-TERM EXAM: QUESTION 4
#vocareum cant refresh. my code is gone so i write what i can quickly here.
def determinant(matrix):
    a = 0
    while a < len(matrix):
        if len(matrix[a]) != len(matrix):
            return None
            break
        a += 1
    if len(matrix) == 1:
        detM = matrix[0][0]
        return detM 
    elif len(matrix) == 2:
        detM = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return detM 
    elif len(matrix) == 3:
