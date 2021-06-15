def determinant(matrix):
    for i in matrix:
        if len(matrix) != len(i):
            return None
        else:
            n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif n == 3:
        first = matrix[0][0]*determinant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]])
        second = matrix[0][1]*determinant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]])
        third = matrix[0][2]*determinant([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]])
        return first-second+third