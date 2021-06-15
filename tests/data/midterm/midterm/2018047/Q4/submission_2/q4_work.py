#4
from copy import deepcopy
def minor(M,i):
    minor = deepcopy(M)
    del minor[0] #Delete first row
    for b in range(len(minor)): #Delete column i
        del minor[b][i]
    return minor
def determinant(M):
    if len(M) == 1: #Base case on which recursion ends
        return M[0][0]
    else:
        determinant = 0
        for x in list(range(len(M))): #Iterates along first row finding cofactors
            determinant += M[0][x] * (-1)**(2+x) * determinant(minor(M,x)) #Adds successive elements times their cofactors
        return determinant