def determinant(matrix):
    if 1<= len(matrix) <= 3:
        for mat in matrix:
            if len(mat) != len(matrix):
                return None
        if len(matrix) == 1:
            out = matrix[0][0]
        if len(matrix) == 2:
            out = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if len(matrix) == 3:
            out = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1])
        return out    
    else:
        return None