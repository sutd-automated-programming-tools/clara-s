def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        a = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return a
    if len(matrix) == 3:
        a = (matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])
        b = (matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])
        c = (matrix[1][0] * matrix[2][1]) - (matrix[2][0] * matrix[1][1])
        d = matrix[0][0] * a - matrix[0][1] * b + matrix [0][2] *c
        return d