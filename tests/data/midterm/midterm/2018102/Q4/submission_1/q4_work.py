def determinant(matrix):
   try: 
    if len(matrix) > 3:
        result = None
    if len(matrix) == 1:
        result = matrix[0]
    if len(matrix) == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) == 3:
        result1 = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        result2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        result3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        result = result1 - result2 + result3
   except:
        result = None
   return result    
        