def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3:
        return None
    for elements in matrix:
        if len(elements) < 1 or len(elements) > 3:
            return None
        if len(elements) != len(matrix):
            return None
    else:
        if len(matrix) == 1:
           for elements in matrix[0]:
                deter = int(elements)
           return deter
        if len(matrix) == 2:
            if len(matrix[0]) != len(matrix[1]):
                   return None
            else:
               deter = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
               return deter
        if len(matrix) ==3:
           if len(matrix[0]) != len(matrix[1]) != len(matrix[2]):
                   return None
           else:
              deter = (matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]))-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]))+(matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]))
              return deter