def determinant(matrix):
    if len(matrix)==1 and len(matrix[0])==1:
        return matrix[0][0]
    elif len(matrix)==2 and len(matrix[0])==2 and len(matrix[1])==2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    elif len(matrix)==3 and len(matrix[0])==3 and len(matrix[1])==3 and len(matrix[2])==3:
        adet = (matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])
        bdet = (matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])
        cdet = (matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])
        return (matrix[0][0]*adet)-(matrix[0][1]*bdet)+(matrix[0][2]*cdet)
    else:
        return None