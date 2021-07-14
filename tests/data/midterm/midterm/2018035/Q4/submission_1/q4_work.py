def determinant(matrix):
    if len(matrix) <1 or len(matrix)>3:
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        if len(matrix[0]) != len(matrix[1]):
            return None
        else:
            return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    else:
        if len(matrix[0]) != len(matrix[1]):
            return None
        a = matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
        b = matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
        c = matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
        return a-b+c