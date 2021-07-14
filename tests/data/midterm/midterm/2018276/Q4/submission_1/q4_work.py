def determinant(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if len(matrix) == 3:
        result = matrix[0][0]*determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]) -\
              matrix[0][1]*determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]) +\
              matrix[0][2]*determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
        return result