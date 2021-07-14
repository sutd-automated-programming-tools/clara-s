def determinant(matrix):
    if len(matrix)<1 or len(matrix)>3:
        return None
    
    for i in range(len(matrix)):
        if len(matrix[0])!=len(matrix[i]):
            return None
    
    if len(matrix)==1:
        det_1=matrix[0][0]
        return det_1
    
    if len(matrix)==2:
        det_2=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return det_2
    
    if len(matrix)==3:
        det_3=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]))+(matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1]))
        return det_3