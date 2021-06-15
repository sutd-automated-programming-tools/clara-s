def determinant(matrix):
    M=matrix
    if len(matrix)!= len(matrix[0]):
        return None
    else:
        if len(matrix)==1:
            det1=matrix[0][0]
        elif len(matrix)==2:
            det1=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        elif len(matrix)==3:
            a=M[0][0]
            b=M[0][1]
            c=M[0][2]
            d=M[1][0]
            e=M[1][1]
            f=M[1][2]
            g=M[2][0]
            h=M[2][1]
            i=M[2][2]
            det1=a*e*i-a*h*f-b*d*i+b*g*f+c*d*h-c*e*g
    return det1