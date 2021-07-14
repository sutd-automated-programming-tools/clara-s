def determinant(matrix):
    if len(matrix)!=len(matrix[0]) or len(matrix)<1 or len(matrix)>3:
        return None
    else:
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            ad = matrix[0][0]*matrix[1][1]
            bc = matrix[0][1]*matrix[1][0]
            return ad-bc
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
            det = a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-g*e)
            return det
        