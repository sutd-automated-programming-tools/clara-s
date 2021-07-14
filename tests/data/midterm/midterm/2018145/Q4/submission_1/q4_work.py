def determinant(matrix):
    n = len(matrix[0])
    if len(matrix)!=n or n<1 or n>3:
        return None
    det = 0
    if n==1:
        det = matrix[0][0]
    elif n==2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det1 = matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2]
        det2 = matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2]
        det3 = matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1]
        det = matrix[0][0]*det1 - matrix[0][1]*det2 + matrix[0][2]*det3
    return det