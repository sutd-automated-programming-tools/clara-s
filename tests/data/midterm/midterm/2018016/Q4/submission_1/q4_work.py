def determinant(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row != col:
        return
    else:
        if len(matrix) == 1:
            for i in matrix:
                return matrix[0][0]
        elif len(matrix) == 2:
            det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
            return det
        else:
#            firstcoeff = matrix[0[0]
#            secondcoeff = matrix[0][1]
#            return secondcoeff
#            thirdcoeff = matrix[0][2]
            first = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            second = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            third = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            total = first - second + third
            return total
    