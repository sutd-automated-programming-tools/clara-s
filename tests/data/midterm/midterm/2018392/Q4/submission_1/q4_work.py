def determinant(matrix):
    n=len(matrix)
    m=len(matrix[0])
    if n not in range (1,4):
        return None
    elif m!=n:
        return None
    elif n == 1:
        det=matrix[0][0]
    elif n==2:
        det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif n==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        i=matrix[2][2]
        det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    return det