def determinant(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return None
    if len(matrix) > 3:
        return None
    else:
        if len(matrix) == 1:
            determinant = matrix[0][0]
        elif len(matrix) == 2:
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix) == 3:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            determinant = a * (e * i - f * h ) - b * (d * i - g * f) + c * (d * h - g * e)
    return determinant