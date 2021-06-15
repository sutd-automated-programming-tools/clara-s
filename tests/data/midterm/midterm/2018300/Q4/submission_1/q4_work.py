def determinant(matrix):
    if len(matrix)!=len(matrix[0]):
        return None
    else:
        if len(matrix)==1:
            return int(matrix[0][0])
        elif len(matrix)==2:
            return int(matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1])
        else:
            part1=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
            part2=matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])
            part3=matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
            return int(part1-part2+part3)