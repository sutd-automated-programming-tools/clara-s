def determinant(matrix):
         if len(matrix) == 1 :
             return matrix[0][0] 
         
         elif len(matrix) == 2:
             if len(matrix[0]) == len(matrix[1]) :
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
             else :
                return None
         elif len(matrix) == 3 :
            if len(matrix[0]) == len(matrix[1]) and len(matrix[1]) == len(matrix[2]) and len(matrix[0]) == len(matrix[2]):
              return  matrix[0][0]* (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -  matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            else :
                return None
         else :
             return None