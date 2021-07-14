def determinant(matrix):
    n = len(matrix)
    
    if n == 1:
        det = matrix[0]
        return det
    
    for i in range(n):
        cols = len(matrix[i])
        if cols != n:
            return None
        else:
            continue
        
    if n == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det = int((a * d) - (b * c))
        return det
    
    if n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        
        sub_det1 = (matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])
        sub_det2 = (matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])
        sub_det3 = (matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])
        
        det = (a * sub_det1) - (b * sub_det2) + (c * sub_det3)
        return int(det)