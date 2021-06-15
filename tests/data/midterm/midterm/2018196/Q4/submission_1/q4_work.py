def determinant(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    
    if rows == 1 and col == 1:
        det_m = matrix [0][0]
        return det_m
    
    elif rows == 2 and col == 2:
        det_m = (matrix [0][0] * matrix [1][1]) - (matrix [0][1] * matrix [1][0])
        return det_m
    
    elif rows == 3 and col == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        
        det_m = a*((e*i)-(f*h)) - b*((d*i)-(f*g)) + c*((d*h)-(e*g))
        return det_m
    else:
        return None