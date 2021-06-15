def determinant(matrix):
    nested = len(matrix)
    if nested == 1:
        det = matrix[0]
    elif nested != 1:
        if nested <= 3 and nested >= 1:
            for i in range(len(matrix)):
                innest = len(matrix[i])
        if nested == innest:
            pass
        else:
            return None
    if nested == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif nested == 3:
        det1 = matrix[0][0] * (matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])
        det2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])
        det3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        det = det1 - det2 + det3
    else:
        pass
    return det