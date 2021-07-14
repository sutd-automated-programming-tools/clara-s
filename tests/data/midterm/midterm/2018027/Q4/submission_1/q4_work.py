def determinant(matrix):
    m = matrix
    if len(matrix) == len(matrix[0]) and len(matrix)<=3 and len(matrix)>0:
        n = len(matrix)
        if n == 1:
            return m[0][0]
        elif n == 2:
            return (m[0][0]*m[1][1]-m[0][1]*m[1][0])
        elif n == 3:
            return m[0][0]*determinant([m[1][1:],m[2][1:]])-m[0][1]*determinant([[m[1][0],m[1][2]],[m[2][0],m[2][2]]])+m[0][2]*determinant([m[1][:2],m[2][:2]])