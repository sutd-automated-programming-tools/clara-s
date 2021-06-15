def determinant(matrix):
    if len(matrix)==1 and len(matrix[0])==1:
        result=matrix[0][0]
    elif len(matrix)==2 and len(matrix[0])==2:
        result=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif len(matrix)==3 and len(matrix[0])==3:
        result=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    else:
        result=None
    return result