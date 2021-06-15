def determinant(matrix):
    n = len(matrix)
    if n > 3 or n < 1:
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) != n:
            return None
    else:
        if n == 1:
            deter = matrix[0][0]
        elif n == 2:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            deter = a*d - b*c
        
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
            deter = a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g)
            
        return deter