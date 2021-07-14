def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return None if any(len(matrix[i])!=2 for i in range(len(matrix))) else matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif len(matrix)==3:
        if any(len(matrix[i])!=3 for i in range(len(matrix))):
            return None
        else:
            return matrix[0][0]*determinant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]])-matrix[0][1]*determinant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]])+matrix[0][2]*determinant([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]])
    else:
        return None
    pass