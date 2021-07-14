def determinant(matrix):
    a = len(matrix)
    m = len(matrix[0])
    for i in range(0,a+1):
        n=len(matrix[i])
        if n != m or n != a:
            return None
        else:
            if a == 1:
                return matrix[0][0]
            elif a == 2:
                det2 = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
                return det2
            elif a == 3:
                det3_1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
                det3_2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
                det3_3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
                det3 = matrix[0][0]*det3_1 - matrix[0][1]*det3_2 + matrix[0][2]*det3_3
                return det3