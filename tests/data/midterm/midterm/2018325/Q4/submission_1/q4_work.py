def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    else:
        m = matrix
        if len(m) == 1:
            det = m[0][0]
          
        elif len(m) == 2:
            a = m[0][0]
            b = m[0][1]
            c = m[1][0]
            d = m[1][1]
            
            det = (a*d) - (b*c)
            
        elif len(matrix) == 3:
            a = m[0][0]
            b = m[0][1]
            c = m[0][2]
            d = m[1][0]
            e = m[1][1]
            f = m[1][2]
            g = m[2][0]
            h = m[2][1]
            i = m[2][2]
           
            det = a * (e*i -h*f) - b * (d*i -g*f) + c * (d*h -g*e)
            
    return det
        
        
      