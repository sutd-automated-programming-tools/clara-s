#qn4
def determinant(matrix):
    if ((len(matrix)!=len(matrix[i]) or len(matrix[i])>3 or len(matrix[i])<1) for i in range(len(matrix))): 
            return None
    else:
        if len(matrix)==1:
            return matrix[0][0]
        elif len(matrix)==2:
            return matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
        elif len(matrix)==3:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            return a*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])-b*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])+c*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
