def determinant(matrix):
    n = len(matrix)
    if n<1 or n>3:
        return None
    for i in range(n):
        if len(matrix[i]) != n:
            return None
    
    det =0
    if n == 1:
        det = matrix[0][0]
    
    elif n == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        
    elif n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        
        det_a = a*(e*i - h*f)
        det_b = b*(d*i - g*f)
        det_c = c*(d*h - g*e)
        
        det = det_a - det_b + det_c
    
    return det