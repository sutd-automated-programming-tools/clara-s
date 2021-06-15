def determinant(matrix):
    flaag = True
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            flag = False

    while flag != False
        if len(matrix) == 1: #n=1
            return matrix[0][0]
        if len(matrix) == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det
        if len(matrix) == 3:
            det = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])\
            - matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])\
            + matrix[0][2]* (matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
            return det