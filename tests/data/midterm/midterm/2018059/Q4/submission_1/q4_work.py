def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif len(matrix) == 3:
        x = matrix[0][0]
        y = matrix[0][1]
        z = matrix[0][2]
        a = x*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        b = y*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        c = z*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        det = a - b + c
        return det