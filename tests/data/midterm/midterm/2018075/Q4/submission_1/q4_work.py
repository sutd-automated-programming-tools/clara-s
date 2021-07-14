def determinant(matrix):
    
    if len(matrix[0]) and len(matrix) == 1:
        a = matrix[0][0]
        det_mat = a
        return det_mat
    
    if len(matrix[0]) and len(matrix) == 2:
        if len(matrix[0]) != len(matrix[1]):
            return None
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            det_mat = a*d-b*c
            return det_mat
        
    if len(matrix[0]) and len(matrix) == 3:
        if len(matrix[0]) != len(matrix[1]):
            return None
        elif len(matrix[0]) != len(matrix[2]):
            return None
        elif len(matrix[1]) != len(matrix[2]):
            return None
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            det_mat = a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)
            return det_mat
        
    if len(matrix) == 1:
        if len(matrix) != len(matrix[0]):
            return None
    if len(matrix) == 2:
        if len(matrix) != len(matrix[0]):
            return None
        if len(matrix) != len(matrix[1]):
            return None
    if len(matrix) == 3:
        if len(matrix) != len(matrix[0]):
            return None
        if len(matrix) != len(matrix[1]):
            return None
        if len(matrix) != len(matrix[2]):
            return None
    