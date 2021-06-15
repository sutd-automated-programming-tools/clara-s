def determinant(matrix):
    n = len(matrix)
    if n == 1:
        result = matrix[0][0]
    if n == 2:
        result = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if n == 3:
        result = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][2]*matrix[2][0]-matrix[1][0]*matrix[2][2]) +matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    return result