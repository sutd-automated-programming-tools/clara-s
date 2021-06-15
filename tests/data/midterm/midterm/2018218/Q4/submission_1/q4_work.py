def determinant(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n == m:
        if n == 1:
            det = matrix[0][0]
            return det
        if n == 2:
            det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return det
        if n == 3:
            var1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
            var2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
            var3 = matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1]
            det = matrix[0][0]*var1 - matrix[0][1]*var2 + matrix[0][2]*var3
        return det
    else:
        return None
    