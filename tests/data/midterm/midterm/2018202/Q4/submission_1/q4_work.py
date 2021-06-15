def determinant(matrix):
    for innerls in matrix:
        if len(matrix) != len(innerls):
            return None
        else:
            if len(matrix) == 1:
                return matrix[0][0]
            elif len(matrix) == 2:
                ad = matrix[0][0] * matrix[1][1]
                bc = matrix[0][1] * matrix[1][0]
                return ad-bc
            elif len(matrix) == 3:
                a = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
                b = matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
                c = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
                return a-b+c