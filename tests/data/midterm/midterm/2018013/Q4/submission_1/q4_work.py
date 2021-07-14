def determinant(matrix):
	
    if len(matrix)!=len(matrix[0]):
        return None
    else:
        if len(matrix)==1:
            return matrix[0][0]
        elif len(matrix)==2:
            det=matrix[0][0]*matrix[-1][-1]-matrix[0][1]*matrix[-1][-2]
            return det
        else:
            det=matrix[0][0]*(matrix[1][1]*matrix[-1][-1]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[-1][-1]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
            return det