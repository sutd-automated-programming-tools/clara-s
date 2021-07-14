def determinant(matrix):   
    if len(matrix) ==1: #ensure 1x1
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[1]) ==2 and len(matrix[0]) == 2: #ensure 2x2
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif len(matrix) == 3 and len(matrix[0]) == 3 and len(matrix[1]) == 3 and len(matrix[2]) == 3: # ensure 3x3
        m1 = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]] #set determinants into individual matrices
        m2 = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]
        m3 = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]
        
        return matrix[0][0]*(m1[0][0]*m1[1][1] - m1[0][1]*m1[1][0]) - matrix[0][1]*(m2[0][0]*m2[1][1] - m2[0][1]*m2[1][0]) + matrix[0][2]*(m3[0][0]*m3[1][1] - m3[0][1]*m3[1][0])
    else:
        return None