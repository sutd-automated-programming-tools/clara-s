def determinant(matrix):
    dimen = len(matrix)
    if dimen != len(matrix[0]):
        return None
    
    if dimen == 1:
        return matrix[0][0]
    
    elif dimen == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    elif dimen == 3:
        a = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])
        b = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])
        c = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        return a-b+c
    
    else:
        return None

	