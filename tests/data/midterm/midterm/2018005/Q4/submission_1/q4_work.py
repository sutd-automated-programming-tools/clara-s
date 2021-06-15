def determinant(matrix):
    i = 0
    if len(matrix) > 3 or len(matrix) < 1:
        det =  None
    elif len(matrix) == 1:
        x1 = matrix[0]
        det = x1[0]
    elif len(matrix) == 2:
        for i in matrix:
            det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif len(matrix) == 3:
        for i in matrix:
            x = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
            y = matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
            z = matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][1]))
            det = x - y + z
    return det