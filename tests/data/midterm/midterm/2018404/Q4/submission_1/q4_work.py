def determinant(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row != col:
        return None
    elif row == 1:
        return matrix[0][0]
    elif row == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    else:
        left = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        mid = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        right = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        return (left - mid + right)