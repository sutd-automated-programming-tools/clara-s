def determinant(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return None
    for i in matrix:
        if len(i)==1:
            return i[0]
        elif len(i) == 2:
            determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        elif len(i) == 3:
            determinant = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
    return determinant
