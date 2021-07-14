def determinant(matrix):
    n = len(matrix)
    if n<1 or n >3 :
        return None 
    
    rownumber = len(matrix)
    for row in matrix:
        if len(row) != rownumber:
            return None 
     
    if n == 1:
        return matrix[0]
    if n == 2 :
        return (matrix[0][0]*matrix[1][1] -matrix[0][1]*matrix[1][0])
    
    if n == 3:
        lst = []
        for j in range(len(matrix)):
            lst.append(matrix[j][0])
        
        det2 = matrix[0][1]*matrix[2][2]- matrix[0][2]*matrix[2][1]
        det3 = matrix[0][1]*matrix[1][2]- matrix[0][2]*matrix[1][1]
        
    return (-lst[1]*det2 + lst[2]*det3)
         