def determinant(matrix):
    m = len(matrix[0])
    n = len(matrix)
    if m != n:
        return None
    elif n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        return a*(e*i-h*f) - b*(d*i-g*f) + c*(d*h-g*e)