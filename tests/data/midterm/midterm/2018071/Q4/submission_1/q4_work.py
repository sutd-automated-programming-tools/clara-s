def determinant(matrix):
    if len(matrix) > 3:
        return None
    if len(matrix) < 1:
        return None
    if len(matrix[0]) > 3:
        return None
    if len(matrix[0]) < 1:
        return None
    det = 0
    if len(matrix) == 1:
        det = matrix[0][0]
        return det
    if len(matrix) == 2:
        det = (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
        return det
    if len(matrix) == 3:
        det1 = (matrix[0][0])*(matrix[1][1]*matrix[2][2]- matrix[1][2]*matrix[2][1])
        det2 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])
        det3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
        det = det1 -det2 + det3
        return det