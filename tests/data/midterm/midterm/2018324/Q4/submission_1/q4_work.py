def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 1:
            ans = matrix[0][0]
            return ans
            
        if len(matrix) == 2:
            ans = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return ans
            
        if len(matrix) == 3:
            det1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
            det2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
            det3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
            ans = matrix[0][0]*det1 - matrix[0][1]*det2 + matrix[0][2]*det3
            return ans
    else:
        return None