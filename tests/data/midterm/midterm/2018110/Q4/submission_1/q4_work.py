def determinant(matrix):
    for i in matrix:
        if len(i) == len(matrix):
            if len(matrix)==1:
                det = matrix[0][0]
            elif len(matrix) == 2:
                det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            elif len(matrix) ==3:
                det1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
                det2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
                det3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
                det = matrix[0][0]*det1 - matrix[0][1]*det2 + matrix[0][2]*det3
                
        else:
            return None
    return det