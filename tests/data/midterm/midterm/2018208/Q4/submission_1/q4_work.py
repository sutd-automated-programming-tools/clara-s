def determinant(matrix):
    dim = len(matrix[0])
    for item in matrix:
        if dim != len(item):
            return None
       
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        ad = matrix[0][0]*matrix[1][1]
        bc = matrix[0][1]*matrix[1][0]
        return ad-bc
    if len(matrix) == 3:
        first = matrix[0][0]* (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        second = matrix[0][1]* (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        third = matrix[0][2]* (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
        ans = first - second + third
        return ans