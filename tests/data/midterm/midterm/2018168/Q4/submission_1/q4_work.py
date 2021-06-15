def determinant(matrix):
    n = len(matrix)
   
    determinant=0
    if n >3 or n<1:
        return None
    elif n == 1:
        determinant= matrix[0][0]
    elif n == 2:
        determinant = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    elif n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        det1 = (matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1])
        det2 = (matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])
        det3 = (matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])
        determinant= (a*det1) - (b*det2) + (c*det3)
        
        
      
        
    return determinant