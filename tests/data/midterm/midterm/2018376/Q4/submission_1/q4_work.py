def determinant(matrix):
    row_count = 0
    for row in matrix:
        row_count += 1
    
    for row in matrix:
        column_count = 0
        for col in row:
            column_count += 1
        if row_count != column_count:
            return None
    
    n = row_count
    if n<1 or n>3:
        return None
    
    if n==1:
        det = matrix[0][0]
    
    if n==2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det = a*d - b*c
        
    if n==3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        det = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    
    return det