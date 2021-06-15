def determinant(matrix):
    if len(matrix) == 1:
        if len(matrix[0]) != 1:
            return None
        else:
            return matrix[0][0]

    elif len(matrix) == 2:
        for n in matrix:
            if len(n) != 2:
                return None
                break
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])

    elif len(matrix) == 3:
        for n in matrix:
            if len(n) != 3:
                return None
                break
        return matrix[0][0] * (matrix[1][1] * matrix [2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (matrix[1][0] * matrix [2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix [2][1] - matrix[1][1] * matrix[2][0])
    else:
        return None