def determinant(matrix):
    rows=len(matrix)
    colum=len(matrix[0])
    if rows != colum:
        return None
    if rows <1 or rows>3 or colum<1 or colum >3:
        return None
    if rows==1:
        return matrix[0][0]
    elif rows==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif rows==3:
        mat1=[[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]#ef
        mat2=[[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]#df
        mat3=[[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]#de
        output=matrix[0][0]*determinant(mat1)-matrix[0][1]*determinant(mat2)+matrix[0][2]*determinant(mat3)
        return output