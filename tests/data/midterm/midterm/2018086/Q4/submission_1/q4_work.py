def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return None
        else:
            if len(matrix[i]) == 1:
                return matrix[0][0]
            elif len(matrix[i]) == 2:
                det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
                return det
            elif len(matrix[i]) == 3:
                indet1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
                indet2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
                indet3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
                det2 = matrix[0][0]*indet1 -matrix[0][1]*indet2 + matrix[0][2]*indet3
                return det2