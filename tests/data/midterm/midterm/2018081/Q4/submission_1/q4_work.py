def determinant(matrix):
    #get n from first row to check
    nrow=len(matrix[0])
    for rows in matrix:
        if len(rows)!=nrow:
            return None
            break
    if nrow==1:
        return matrix[0][0]
    elif nrow==2:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[1][0]
        d=matrix[1][1]
        return a*d-b*c
    elif nrow==3:
        a3=matrix[0][0]
        b3=matrix[0][1]
        c3=matrix[0][2]
        d3=matrix[1][0]
        e3=matrix[1][1]
        f3=matrix[1][2]
        g3=matrix[2][0]
        h3=matrix[2][1]
        i3=matrix[2][2]
        det1=e3*i3-f3*h3
        det2=d3*i3-f3*g3
        det3=d3*h3-g3*e3
        return (a3*det1)-(b3*det2)+(c3*det3)
    else: 
        return None