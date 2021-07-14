def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2 and len(matrix[0]) == len(matrix[1]):
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det2 = a*d - b*c
        return det2
        
    elif len(matrix) == 3 and len(matrix[0]) == len(matrix[1]) == len(matrix[2]):
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        det3 = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
        return det3 
    else:
        return None