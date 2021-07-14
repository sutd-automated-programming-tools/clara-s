def determinant(matrix):
    if len(matrix)==1:
        return float(matrix[0][0])
    if len(matrix)==2 and len(matrix[0])==2 and len(matrix[1])==2:
        return float(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    if len(matrix)==3 and len(matrix[0])==3 and len(matrix[1])==3 and len(matrix[2])==3:
        return float((matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+matrix[1][0]*matrix[2][1]*matrix[0][2])-(matrix[2][0]*matrix[1][1]*matrix[0][2]+matrix[1][0]*matrix[0][1]*matrix[2][2]+matrix[0][0]*matrix[2][1]*matrix[1][2]))
    else:
        return None