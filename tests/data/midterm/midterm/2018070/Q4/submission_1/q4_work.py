def determinant(matrix):

    
    if len(matrix) != len(matrix[0]): #make sure num rows = num columns
        return None

    elif len(matrix) == 1:
        det = matrix[0][0]
        return det

    elif len(matrix) ==2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        
        det = a*d - b*c
        return det

    elif len(matrix) ==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        i=matrix[2][2]

        det = a*(e*i - h*f) - b*(d*i - g*f) + c*(d*h - g*e)
        return det
    else:
        return None
    