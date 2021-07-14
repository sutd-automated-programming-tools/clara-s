def determinant(matrix):
    a = len(matrix)    
    for i in matrix:
        b = len(i)
        if b != a:
            return None
    if a == 1:
        return matrix[0][0]
    elif a == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return det
    elif a == 3:
        det = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]) - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+ matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
        return det