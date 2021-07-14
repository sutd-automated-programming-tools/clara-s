def determinant(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(matrix) != len(matrix[i]):
                return None
            elif len(matrix) == 1 and len(matrix[j]) == 1:
                for k in range(len(matrix[j])):
                    det = int(matrix[i][j])
                    return det
            elif len(matrix) == 2 and len(matrix[j]) == 2:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[1][0]
                d = matrix[1][1]
                det = a*d - b*c
                return det
            elif len(matrix) == 3 and len(matrix[j]) == 3:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[0][2]
                #r
                d = matrix[1][0]
                e = matrix[1][1]
                f = matrix[1][2]
                #r
                g = matrix[2][0]
                h = matrix[2][1]
                i = matrix[2][2]
                det = (a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g))
                return det