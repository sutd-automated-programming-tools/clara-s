def determinant(matrix):
    for row in matrix:
        if len(row)!=len(matrix):
            return None
        else:
            if len(row)==1:
                return row[0]
            if len(row)==2:
                det2=matrix[0][0]* matrix[1][1]-matrix[0][1]*matrix[1][0]
                return det2
            if len(row)==3:
                a= matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2])
                b=-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])
                c=matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1])
                det2=a+b+c
                return det2