def determinant(matrix):
    rows=len(matrix)
    if rows>1:
        cols=len(matrix[0])
    else:cols=rows
    if rows>3 or rows<1 or cols!=rows:
        return None
    else:
        
        if rows==1:
            det=matrix[0][0]
            return det
        if rows==2:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[1][0]
            d=matrix[1][1]
            det=a*d-b*c
            return det
        else:
            a=matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            d=matrix[1][0]
            e=matrix[1][1]
            f=matrix[1][2]
            g=matrix[2][0]
            h=matrix[2][1]
            i=matrix[2][2]
            
            det1=e*i-h*f
            det2=d*i-g*f
            det3=d*h-e*g
            
            det=a*det1-b*det2+c*det3
            return det