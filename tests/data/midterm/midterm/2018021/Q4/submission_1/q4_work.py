def determinant(matrix):
    for x in matrix:
        if len(x) != len(matrix):
            return None

    if len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    elif len(matrix[0]) == 3:
        R1 = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        R2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        R3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        return R1 - R2 + R3