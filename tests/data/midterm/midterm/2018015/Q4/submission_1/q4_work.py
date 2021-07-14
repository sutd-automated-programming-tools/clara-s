def det2(a, e, f, h, i):
    det = a * (e * i - f * h)
    return det

def determinant(matrix):
#	if dimension is not nxn for 1<=n<=3, return False
    if len(matrix) < 1 or len(matrix) > 3:
        return None
    
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    
    elif len(matrix) == 2:
        for row in matrix:
            if len(row) != 2:
                return None
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    
    elif len(matrix) == 3:
        for row in matrix:
            if len(row) != 3:
                return None
        first = det2(matrix[0][0], matrix[1][1], matrix[1][2], matrix[2][1], matrix[2][2])
        second = det2(matrix[0][1], matrix[1][0], matrix[1][2], matrix[2][0], matrix[2][2])
        third = det2(matrix[0][2], matrix[1][0], matrix[1][1], matrix[2][0], matrix[2][1])
        finaldet = first - second + third
        return finaldet