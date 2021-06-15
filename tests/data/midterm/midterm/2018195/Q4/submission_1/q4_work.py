def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        det = matrix[0][0]
        return det

    if len(matrix) == 2:
        if len(matrix) == len(matrix[0]) and len(matrix) == len(matrix[1]):
            det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return det
        else:
            return None
        
    if len(matrix) == 3:
        if len(matrix) == len(matrix[0]) and len(matrix) == len(matrix[1]) and len(matrix) == len(matrix[2]):
            det = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
            return det
        else:
            return None
            