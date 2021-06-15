def determinant(matrix):
    
    n = len(matrix)
    
    #if n outside of 1<=n<=3
    if n<1 or n>3:
        return None
    
    #if not nxn matrix
    for i in matrix:
        if n != len(i):
            return None
        
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return ((matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]))
    
    if n == 3:
        part_1 = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        part_2 = matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        part_3 = matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        
        return part_1 - part_2 + part_3