def size_of_matrix(matrix):
    if len(matrix)!=len(matrix[0]):
        return None
    else:
        n=len(matrix)
        return n
def determinant(matrix):
	
    if size_of_matrix (matrix)== 1:
        return matrix[0][0]
    elif  size_of_matrix (matrix) == 2:
        ans=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return ans
    elif  size_of_matrix (matrix) == 3:
        ans=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]) - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        return ans
    else:
        return None
                          
        
    