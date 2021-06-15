def determinant(matrix):
    dim = len(matrix[0])
    for i in range(len(matrix)):
        if len(i) != dim:
            return None
    if dim < 1 or dim > 3:
        return None
    elif dim == 1:
        return matrix[0][0]
    elif dim == 2:
        det =  (matrix[1][1]) * (matrix[2][2]) - (matrix[1][2]) * (matrix[2][1])
        return det
    elif dim == 3:
        det1 = (matrix[1][1]) * ((matrix[2][2]) * (matrix[3][3]) - (matrix[2][3]) * (matrix[3][2]))
        det2 = (matrix[1][2]) * ((matrix[2][1]) * (matrix[3][3]) - (matrix[2][3]) * (matrix[3][1]))
        det3 = (matrix[1][3]) * ((matrix[2][1]) * (matrix[3][2]) - (matrix[2][2]) * (matrix[3][1]))
        det = det1 - det2 + det3
        return det