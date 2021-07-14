def determinant(matrix):
    length = len(matrix[0])
    for row in matrix:
        if not len(row)==length:
            return None 
        else:
            if len(matrix)==1:
                det = matrix[0][0]
                return det
            
            if len(matrix)==2:
                col=matrix[0][0]
                col1=matrix[1][1]
                row1=matrix[0][1]
                row2=matrix[1][0]
                det1 = (col*col1)-(row1*row2)
                return det1
            
            if len(matrix)==3:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[0][2]
                e = matrix[1][1]
                i = matrix[2][2]
                f = matrix[1][2]
                h = matrix[2][1]
                d = matrix[1][0]
                g = matrix[2][0]
                det2 = a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g))
                return det2