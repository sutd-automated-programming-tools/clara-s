def determinant(matrix):
    detM = 0
    if len(matrix) == 1: #for if n equal 1
        detM = matrix[0][0] #detM will be the value of the matrix itself
        
    elif len(matrix) == 2: #for if n = 2
        detM = (matrix[0][0][0]*matrix[0][1][1])-(matrix[0][0][1]*matrix[0][1][0]) 
        #detM will be the (first list first value multiplied by the second list second value) subtract the (first list second value multiplied by the second list first value)
    
    elif len(matrix) == 3:
        a = matrix[0][0][0]
        b = matrix[0][0][1]
        c = matrix[0][0][2]
        deta = (matrix[0][1][1]*matrix[0][2][2])-(matrix[0][1][2]*matrix[0][2][1])
        detb = (matrix[0][1][0]*matrix[0][2][2])-(matrix[0][1][2]*matrix[0][2][0])
        detc = (matrix[0][1][0]*matrix[0][2][1])-(matrix[0][1][1]*matrix[0][2][0])
        detM = a*deta - b*detb + c*detc
        
    else:
        return None
    
    return detM
