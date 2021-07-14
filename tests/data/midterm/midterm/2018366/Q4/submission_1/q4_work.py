def determinant(matrix):
    if len(matrix)!=len(matrix[0]):
        return None
    elif len(matrix)==1:
        a=matrix[0][0]
        return a
    elif len(matrix)==2:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[1][0]
        d=matrix[1][1]
        return a*d-b*c
    else:
        a,b,c=matrix[0]
        d,e,f=matrix[1]
        g,h,i=matrix[2]
        return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)