def determinant(matrix):
    det = 0
    d31 = 0
    d32 = 0
    d33 = 0
    n = len(matrix)
    if n < 1 or n > 3:
        return None
    if n == 1:
        det = matrix[0][0]
    elif n == 2:
        for i in matrix:
            if len(i) != 2:
                return None
        det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif n == 3:
        for i in matrix:
            if len(i) != 3:
                return None
        d31 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])
        d32 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        d33 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        det = d31 -d32 + d33
    return det