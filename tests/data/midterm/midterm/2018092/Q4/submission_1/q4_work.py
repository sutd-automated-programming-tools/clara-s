def determinant(matrix):
    if len(matrix) > 3:
        return None
    
    elif len(matrix) == 1:
        return matrix[0][0]
    
    elif len(matrix) == 2:
        #2by2 matrix = [[a,b],[c,d]]
        det2 = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
        return det2
    
    elif len(matrix) == 3:
        #3by3 matrix = [[a,b,c],[d,e,f],[g,h,i]]
        m = matrix
        # print(m[1][1])
        d1 = (m[1][1]*m[2][2])-(m[1][2]*m[2][1])
        d2 = (m[1][0]*m[2][2])-(m[1][2]*m[2][0])
        d3 = (m[1][0]*m[2][1])-(m[1][1]*m[2][0])
        det3 = (m[0][0]*d1) - (m[0][1]*d2) + (m[0][2]*d3)
        return det3
    else:
        return None