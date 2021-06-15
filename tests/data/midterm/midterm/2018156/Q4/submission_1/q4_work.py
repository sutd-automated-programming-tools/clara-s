def determinant(matrix):
    
    if len(matrix) <1 or len(matrix) > 3:
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return None
        
    if len(matrix) == 1 :
        return int(matrix[0])
    
    if len(matrix) == 2 :
        return float( (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))
    
    if len(matrix) == 3 :
        a = [ int([matrix[1][1]) , int(matrix[1][2]) ] ,[ int(matrix[2][1]) , int(matrix[2][2]) ] ] 
        b = [ int([matrix[1][0]) , int(matrix[1][2]) ] ,[ int(matrix[2][0]) , int(matrix[2][2]) ] ]
        c = [ int([matrix[1][0]) , int(matrix[1][1]) ] ,[ int(matrix[2][0]) , int(matrix[2][1]) ] ]
        d = int(matrix[0][0]) * determinant(a)
        e = int(matrix[0][1]) * determinant(b)
        f = int(matrix[0][2]) * determinant(c)
        return (d-e+f)