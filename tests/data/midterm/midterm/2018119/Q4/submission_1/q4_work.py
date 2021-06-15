def determinant(matrix):
    sz = len(matrix)
    if (sz>3 or sz<1):
        return None
    for row in matrix:
        if len(row) != sz:
            return None
    if sz == 1:
        det = matrix[0][0]
    elif sz == 2:
        det = matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
    elif sz == 3:
        A = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        B = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        C = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        det = A-B+C
    return det