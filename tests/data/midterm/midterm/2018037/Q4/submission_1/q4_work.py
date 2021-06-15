def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        if len(matrix[0])==2 and len(matrix[1])==2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        else:
            return None
    elif len(matrix)==3:
        if len(matrix[0])==3 and len(matrix[1])==3 and len(matrix[2])==3:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            d=matrix[1][0]
            e=matrix[1][1]
            f=matrix[1][2]
            g=matrix[2][0]
            h=matrix[2][1]
            i=matrix[2][2]
            return (a*determinant([[e,f],[h,i]]))-(b*determinant([[d,f],[g,i]]))+(c*determinant([[d,e],[g,h]]))
        else:
            return None
    return None