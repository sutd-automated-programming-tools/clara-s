def determinant(matrix):
    rowcount = len(matrix)
    if rowcount == 1:
        return matrix[0][0]
    columncount = len(matrix[0])
    if rowcount != columncount:
        return None
    if rowcount == 2 and columncount == 2:
        det = (matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])
        return det
    if rowcount == 3 and columncount == 3:
        det1 = matrix[0][0]*((matrix[1][1]*matrix[2][2]) - (matrix[2][1]*matrix[1][2]))
        det2 = matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[2][0]*matrix[1][2]))
        det3 = matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[2][0]*matrix[1][1]))
        return det1 - det2 + det3