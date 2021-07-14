def determinant(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return None
    if len(matrix) == 1:
        det = matrix[0][0]
    elif len(matrix) == 2:
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1]  * matrix[1][0])
    elif len(matrix) == 3:
        coa = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])
        cob = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])
        coc = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1])
        det = coa - cob + coc
    return det