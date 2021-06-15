def determinant(matrix):
    n=len(matrix)
    for i in range(n-1):
        if len(matrix[i])!=n:
            return None
    if n==1:
        det=matrix[0][0]
    if n==2:
        det=((matrix[0][0])*(matrix[1][1]))-((matrix[0][1])*(matrix[1][0]))
    if n==3:
        det1=((matrix[1][1])*(matrix[2][2]))-((matrix[1][2])*(matrix[2][1]))
        det2=((matrix[1][0])*(matrix[2][2]))-((matrix[2][0])*(matrix[1][2]))
        det3=((matrix[1][0])*(matrix[2][1]))-((matrix[1][1])*(matrix[2][0]))
        det=(matrix[0][0])*det1-(matrix[0][1])*det2+(matrix[0][2])*det3
    return det