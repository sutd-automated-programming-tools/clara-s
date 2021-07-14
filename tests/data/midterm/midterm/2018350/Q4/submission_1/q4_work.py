def determinant(matrix):
    if len(matrix)<1 or len(matrix)>3:
        return None
    elif len(matrix) != len(matrix[0]):
        return None
    elif len(matrix)==1:
        ans = matrix[0][0]
    elif len(matrix) == 2:
        ans= matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif len(matrix) == 3:
        ans = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
    return ans