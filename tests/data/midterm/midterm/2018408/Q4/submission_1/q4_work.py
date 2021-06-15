
def determinant(matrix):
    if len(matrix) >= 1 and len(matrix) <= 3:
        for i in range(len(matrix)):
            if len(matrix) != len(matrix[i]):
                return None
            if len(matrix) == 1:
                det = matrix[0][0]
            elif len(matrix) == 2:
                det = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
            else:
                det = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]) - matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]) + matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
        return det
    else:
        return None