def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return None
        else:
            pass
    if len(matrix) == 1:
        det = matrix[0][0]
        return det
    elif len(matrix) == 2:
        det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return det
    else:
        det_a = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        det_b = -matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        det_c = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
        det_t = det_a + det_b + det_c
        return det_t
