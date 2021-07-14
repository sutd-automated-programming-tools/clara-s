def determinant(matrix):
    #check that matrix is nxn
    n = len(matrix)
    for i in range(len(matrix)):
        if len(matrix[i]) != n:
            return None
    #finding det
    if n == 1:
        det = matrix[0][0]
    elif n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        a = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        b = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        c = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        det = a-b+c
    return det