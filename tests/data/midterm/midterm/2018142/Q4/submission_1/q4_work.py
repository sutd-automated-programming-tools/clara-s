def determinant(matrix):
    for i in matrix:
        a = len(matrix)
        b = len(i)
        if a!=b:
            return None
    if a == 1:
       det = matrix[0][0]
       return det
    if a == 2:
        det =( matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
        return det
    if a ==3:
        m1=(matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]))
        m2=(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]))
        m3=(matrix[0][2]*((matrix[1][1]*matrix[2][1]-matrix[1][1]*matrix[2][0])))
        det = m1-m2+m3
        return det