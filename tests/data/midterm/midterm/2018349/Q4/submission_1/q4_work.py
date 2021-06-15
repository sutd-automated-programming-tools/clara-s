def determinant(matrix):
    if len(matrix) >= 1 and len(matrix) <= 3:
        for row in matrix:
            if len(row) == len(matrix):
                if len(matrix) == 1:
                    return matrix[0][0]*len(row)
                elif len(matrix) == 2:
                    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
                elif len(matrix) == 3:
                    return matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
            else:
                return None