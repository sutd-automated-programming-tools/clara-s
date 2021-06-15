def determinant(matrix):
    if len(matrix)==1:
        return(matrix[0][0])
    if len(matrix)==2:
        if len(matrix[0])==len(matrix[1])==2:
            return(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
        else:
            return None
    if len(matrix)==3:
        if len(matrix[0])==len(matrix[1])==len(matrix[1])==3:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            a11=matrix[1][1]
            a12=matrix[1][2]
            a21=matrix[2][1]
            a22=matrix[2][2]
            b11=matrix[1][0]
            b12=matrix[1][2]
            b21=matrix[2][0]
            b22=matrix[2][2]
            c11=matrix[1][0]
            c12=matrix[1][1]
            c21=matrix[2][0]
            c22=matrix[2][1]
            return (a*(a11*a22-a21*a12)-b*(b11*b22-b21*b12)+c*(c11*c22-c12*c21))
        