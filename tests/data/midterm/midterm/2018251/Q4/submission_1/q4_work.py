def determinant(matrix):
    det = 0
    if len(matrix[0]) !=  len(matrix):
        return None
    if len(matrix[0]) == 1:
        det = matrix[0][0]
    elif len(matrix[0]) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif len(matrix[0]) == 3:
        det = matrix[0][0]*((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])) - matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[2][0]*matrix[1][2])) + matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[2][0]*matrix[1][1]))     
    return det
