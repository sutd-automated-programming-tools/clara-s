def determinant(matrix):
    if len(matrix)!=len(matrix[0]):
        return None
    elif len(matrix)==1:
        output=matrix[0][0]
        return output
    elif len(matrix)==2:
        output=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return output
    elif len(matrix)==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        i=matrix[2][2]
        output=a*(e*i-h*f)-b*(d*i-f*g)+c*(d*h-g*e)
        return output
    else:
        return None
     