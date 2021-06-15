def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) < 1 or len(matrix) >3:
        return None
    elif len(matrix[0]) < 1 or len(matrix[0]) > 3:
        return None
    else:
        if len(matrix) == 1:
            determinant = matrix[0][0]
            return determinant
        elif len(matrix) == 2:
            determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return determinant
        elif len(matrix) == 3:
            term1 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
            term2 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
            term3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
            determinant = term1 - term2 + term3
            return determinant
    