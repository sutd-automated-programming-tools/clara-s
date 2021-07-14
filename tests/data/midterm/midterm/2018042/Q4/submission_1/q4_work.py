def determinant(matrix):
    
    n=len(matrix)
    for i in matrix:
        if len(i) != n:
            return None
       
    if n==1:
        det=matrix[0][0]
    elif n==2:
        
        det=matrix[0][0] * matrix[-1][-1]-matrix[0][-1] * matrix[-1][0]
    elif n==3:
        det=matrix[0][0]*(matrix[1][1] *matrix[2][2]-matrix[1][2] *matrix[2][1]) - matrix[0][1]*(matrix[1][0] *matrix[2][2]-matrix[2][0] *matrix[1][2]) + matrix[0][2]*(matrix[1][0] *matrix[2][1]-matrix[2][0] *matrix[1][1])
    else:
        return None
    return det
	