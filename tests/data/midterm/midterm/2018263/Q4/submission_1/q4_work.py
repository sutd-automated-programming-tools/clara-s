def determinant(matrix):
    m=len(matrix)
    determine=1
    for i in matrix:
        n=0
        for j in i:
            n+=1
        if n!=m:
            determine=0
    if determine==0:
        re=None
    elif m==n==1:
        re=matrix[0][0]
    elif m==n==2:
        re=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif m==n==3:
        re=matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    else:
        re=None
    return re
    pass