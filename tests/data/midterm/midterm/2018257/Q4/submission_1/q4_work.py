def determinant(matrix):
    for a in matrix:
        if len(matrix) != len(a):
            return None
    for i in matrix:
        if len(i) <1 or len(i) > 3:
            return None 
        if len(i)==1:
            return i[0]
        if len(i) == 2:
            det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return det
        if len(i) == 3:
            det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
            return det