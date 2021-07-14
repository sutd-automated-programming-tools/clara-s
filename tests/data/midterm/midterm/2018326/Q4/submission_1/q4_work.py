def determinant(matrix):
    n=len(matrix)
    if n!=0 and len(matrix[0])!=len(matrix[1]):
        return None
    if n<1 or n>3:
        return None
    else:
        if n==1:
            d=matrix[0][0]
        elif n==2:
            d=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        elif n==3:
            d=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    return d
