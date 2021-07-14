def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return None
        else:
            if len(matrix) == 1:
                return matrix[0][0]
            elif len(matrix) == 2:
                return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
            else:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[0][2]
                det1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
                det2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
                det3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
                return a*det1 - b*det2 + c*det3