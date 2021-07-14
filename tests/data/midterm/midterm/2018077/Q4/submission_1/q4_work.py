def determinant(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    if rows!=cols:
        return None
    if rows<0 or rows>4:
        return None
    if cols<0 or cols>4:
        return None
    elif rows==1 and cols==1:
        return matrix[0][0]
    elif rows==2 and cols==2:
        return ((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))
    elif rows==3 and cols==3:
        return (matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]))-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]))+(matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]))