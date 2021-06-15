def determinant(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if m != n:
        return None
    if m != 1 and m != 2 and m != 3:
        return None
    else:
        
        if m == 1:
            return matrix[0][0]
        elif m == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        elif m ==3:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            return (a*e*i - a*h*f - b*d*i + b*g*f + c*d*h - c*g*e)