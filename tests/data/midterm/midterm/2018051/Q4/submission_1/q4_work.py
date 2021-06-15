
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    elif len(matrix) == 3:
        first = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2]*matrix[2][1])
        second = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2]*matrix[2][0])
        third = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1]*matrix[2][0])
        det = first - second + third
        return det