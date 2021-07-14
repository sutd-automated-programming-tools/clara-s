def determinant(matrix):
    if len(matrix)==1:
        x=matrix[0][0]
        return x
    for i in range(len(matrix)):
        if len(matrix[i-1])!=len(matrix[i]) or len(matrix[i])>=4:
            return None
    if len(matrix)==2:
        return det(matrix)
    if len(matrix)==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        j=matrix[2][2]
        dete=a*det([[e,f],[h,j]])-b*det([[d,f],[g,j]])+c*det([[d,e],[g,h]])
        return dete
def det(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]