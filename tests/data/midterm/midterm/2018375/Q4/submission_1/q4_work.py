def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3:
        return None
    if len(matrix) != len(matrix[0]):
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return a*d - b*c
    if len(matrix) == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        return a*(e*i - h*f) - b*(d*i - g*f) + c*(d*h - g*e)