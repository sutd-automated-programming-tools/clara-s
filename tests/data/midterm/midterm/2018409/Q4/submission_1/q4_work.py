def determinant(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return None
    elif n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        fm = [matrix[1][1:], matrix[2][1:]]
        sm = [matrix[1][::2], matrix[2][::2]]
        tm = [matrix[1][0:2], matrix[2][0:2]]
        first = matrix[0][0] * determinant(fm)
        second = matrix[0][1] * determinant(sm)
        third = matrix[0][2] * determinant(tm)
        return first - second + third