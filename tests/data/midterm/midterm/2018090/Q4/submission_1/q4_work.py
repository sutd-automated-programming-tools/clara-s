def determinant(matrix):
    if matrix==[]:
        return None
    for row in matrix:
        if len(matrix)==1:
            det=row[0]
            return det
        elif len(matrix)==2 and len(row)==2:
            det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
            return det
        elif len(matrix)==3 and len(row)==3:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            d=matrix[1][0]
            e=matrix[1][1]
            f=matrix[1][2]
            g=matrix[2][0]
            h=matrix[2][1]
            i=matrix[2][2]
            det=a*(e*f-h*i)-b*(d*i-f*g)+c*(d*h-e*g)
            return det
        
        else:
            return None