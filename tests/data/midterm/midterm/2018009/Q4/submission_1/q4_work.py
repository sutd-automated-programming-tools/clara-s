def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            a = matrix[0][0]
            d = matrix[1][1]
            b = matrix[0][1]
            c = matrix[1][0]
            ans = a*d - b*c
            return ans
        elif len(matrix) == 3 :
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            ans = (a*((e*i) - (f*h))) - (b*((d*i) - (f*g))) + (c*((d*h) -(e*g)))
            return ans
        else:
            return None
    else:
        return None