def determinant(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return None
    elif n == 1:
        det = matrix[0][0]
        return det
    elif n == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det = (a*d) - (b*c)
        return det
    elif n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        det = (a * ((e*i) - (f*h))) - (b * ((d*i) - (f*g))) + (c * ((d*h) - (e*g)))
        return det
    