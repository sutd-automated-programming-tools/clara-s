def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3 and len(matrix[0]) == 3:
        row_1 = matrix[0]
        row_2 = matrix[1]
        row_3 = matrix[2]
        det1 = row_1[0] * (row_2[1] * row_3[2] - row_2[2] * row_3[1])
        det2 = -1 * row_1[1] * (row_2[0] * row_3[2] - row_2[2] * row_3[0])
        det3 = row_1[2] * (row_2[0] * row_3[1] - row_2[1] * row_3[0])
        return det1 + det2 + det3
    else:
        return None