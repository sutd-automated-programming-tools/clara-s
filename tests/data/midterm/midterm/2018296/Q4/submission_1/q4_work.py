def determinant(matrix):
    while True:
        try:
            l = len(matrix)
            
            if l == 1:
                det = matrix[0][0]
                
            elif l == 2:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[1][0]
                d = matrix[1][1]
                det = (a*d)-(b*c)
            
            elif l == 3:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[0][2]
                d = matrix[1][0]
                e = matrix[1][1]
                f = matrix[1][2]
                g = matrix[2][0]
                h = matrix[2][1]
                i = matrix[2][2]
                j = determinant([[e, f], [h, i]])
                k = determinant([[d, f], [g, i]])
                l = determinant([[d, e], [g, h]])
                det = (a*j) - (b*k) + (c*l)
            return det
        except IndexError:
            return None