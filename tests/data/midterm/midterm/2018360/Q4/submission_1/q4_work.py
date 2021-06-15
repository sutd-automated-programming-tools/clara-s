def determinant(matrix):
    for i in matrix:
        if len(i) == 1:
            for j in i:
                return j
        elif len(i) == 2:
            if len(matrix[0]) - len(matrix[1]) < 0 or len(matrix[0]) - len(matrix[1]) > 0:
                return None
            else:
                return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            return matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])