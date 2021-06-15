def determinant(matrix):
    for i in matrix:
        if len(matrix) != len(i):
            return None
        else:
            if len(matrix) == 1:
                det = i[0]
                return det
            if len(matrix) == 2:
                a=list(matrix[0]+matrix[1])
                det = a[0]*a[-1] - a[1]*a[-2]
                return det
            if len(matrix) == 3:
                a = list(matrix[1]+matrix[2])
                b1 = a[1]*a[-1] - a[2]*a[-2]
                b2 = a[0]*a[-1] - a[2]*a[-3]
                b3 = a[0]*a[-2] - a[1]*a[-3]
                b = [b1,-b2,b3]
                c = matrix[0]
                det = c[0]*b[0] + c[1]*b[1] + c[2]*b[2]
                return det
                    
