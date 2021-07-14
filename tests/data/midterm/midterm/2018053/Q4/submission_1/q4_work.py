import copy 

def minor(matrix,i):
    A = matrix
    minor = copy.deepcopy(A)
    del minor[0] 
    for b in range(len(minor)): 
        del minor[b][i]
    return minor

def determinant(matrix):
    A = matrix
    if len(A) == 1: 
        return A[0][0]
    elif len(A) == 2 or 3:
        det = 0
        for x in list(range(len(A))): 
            det += A[0][x] * (-1)**(2+x) * determinant(minor(A,x)) 
        return det