def determinant (matrix):
    n = len(matrix[0])
    if n<1 or n>3:
        return None
    if n != (len(matrix)):
        return None
    
    if n == 1:
        return matrix[0][0]

    if n == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        return det
    
    if n ==3:
        det = matrix[0][0]*( matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - matrix[0][1]*( matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]) + matrix[0][2]*( matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
        return det