def determinant(matrix):
    det=0
    if len(matrix)>3:
        return None
    elif len(matrix)<1:
        return None
    for i in matrix:
        if len(matrix)==1:
            det=matrix[0][0]
        if len(matrix)==2:
            det= matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        if len(matrix)==3:
            det= matrix[0][0]*((matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]))-matrix[0][1]*((matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]))+matrix[0][2]*((matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]))
                
    return det