def determinant(matrix):
	pass

def determinant (matrix):
    
        
    if len(matrix) not in range(1,4):
        return None
    if len(matrix) == 1 :
        det = matrix[0][0]
    elif len(matrix)== 2:
        if len(matrix[0]) == len(matrix[1]):
            
            det = (matrix[0][0])*(matrix[1][1]) - (matrix[0][1])*(matrix[1][0])
    elif len(matrix) == 3:
        #for i in matrix:
        det1 = matrix[0][0]*(matrix[1][1])*(matrix[2][2]) - (matrix[1][2])*(matrix[2][1])
        det2 = matrix[0][1]*(matrix[1][0])*(matrix[2][2]) - (matrix[1][2])*(matrix[2][0])
        det3 = matrix[1][0]*(matrix[2][1])*(matrix[2][2]) - (matrix[1][1])*(matrix[2][0])
        det = det1 -det2 + det3
        
    return det