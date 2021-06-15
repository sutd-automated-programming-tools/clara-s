def determinant(matrix):
    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:  
            return None
    det  = 0
    if n == 1:
        det = matrix[0][0]
    elif n == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det += matrix[0][0] * ( matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        det -= matrix[0][1] * ( matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) 
        det += matrix[0][2] * ( matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
     
    return det
