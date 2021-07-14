def determinant(matrix):
    if (len(matrix) < 1) or (len(matrix) > 3):
        return None
    else:
        for i in matrix:
            #if these are two sublist in the matrix, compute determinant
            if (len(matrix == 2)):
                for item in i:
                    value_1 = item[0] * item[1]
                    value_2 = item[1] * item[0]
                    new_value = value_1 - value_2
             #elif there are 3 sublist in the matrix, compute determinant
            
        return new_value
    

print(determinant([[100]]))

print(determinant([[-5, -4], [-2, -3]])
      
print(determinant([[2, -3, 1], [2, 0, 1], [1, 4, 5]])

print(determinant([[0, 3, 5], [5, 5, 2], [3, 4, 3]]))
     