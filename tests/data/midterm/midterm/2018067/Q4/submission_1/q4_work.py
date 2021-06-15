def determinant(matrix):
    if len(matrix) == 1:
        for i in matrix:
            for j in i:
                return j
    elif len(matrix) == 2:
        for i in matrix:
            if len(i) != 2:
                return None     
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det = a*d - b*c
        return det
    elif len(matrix) ==3:
        for i in matrix:
            if len(i) != 3:
                return None
            
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        first = a *(e*i-f*h)
        second = b *(d*i-f*g)
        third = c*(d*h-e*g)
        ans = first-second+third
        return ans

    else:
        return None