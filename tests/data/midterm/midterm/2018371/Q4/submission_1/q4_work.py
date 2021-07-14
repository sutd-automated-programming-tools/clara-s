def determinant(matrix):
    m = len(matrix)
    n1 = len(matrix[0])
    if m != n1:
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        ad = matrix[0][0] * matrix[1][1]
        bc = matrix[0][1] * matrix[1][0]
        return ad - bc
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
        aei = a*e*i
        ahf = a*h*f
        bdi = b*d*i
        bgf = b*g*f
        cdh = c*d*h
        cge = c*g*e
        return aei-bdi+cdh-ahf+bgf-cge