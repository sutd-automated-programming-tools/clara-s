def determinant(matrix):

    for i in range(len(matrix) - 1):
        if len(matrix) != len(matrix[i]):
            print ("Not square!")
            return None
        else:

            if len(matrix) == 1:
                print ("1 x 1 Matrix")
                a = matrix [0][0]
                return a
            elif len(matrix) == 2:
                print ("2 x 2 matrix")
                a = matrix [0][0]
                b = matrix [0][1]
                c = matrix [1][0]
                d = matrix [1][1]
                return ((a*d) - (b*c))
            elif len(matrix) == 3:
                print ("three by three!")
                a = matrix [0][0]
                b = matrix [0][1]
                c = matrix [0][2]
                d = matrix [1][0]
                e = matrix [1][1]
                f = matrix [1][2]
                g = matrix [2][0]
                h = matrix [2][1]
                i = matrix [2][2]
                adet = a * ((e*i) - (f*h))
                bdet = b * ((d*i)-(f*g))
                cdet = c * ((d*h)-(e*g))
                return (adet -bdet + cdet)
            else:
                print("out of 1 to 3 range!")
                pass