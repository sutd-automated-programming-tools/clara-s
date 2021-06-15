def determinant(matrix):
    n1=len(matrix)
    n2=len(matrix[0])
    if n1 == n2:
        if n1 == 1:
            det = matrix[0][0]
        elif n1 == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif n1 == 3:
            det = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] + matrix[0][2] * matrix[1][0] * matrix[2][1] - (matrix[2][0] * matrix[1][1] * matrix[0][2] + matrix[2][1] * matrix[1][2] * matrix[0][0] + matrix[2][2] * matrix[1][0] * matrix[0][1])
        return det
    else:
        return None