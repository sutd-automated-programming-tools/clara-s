def by2matrix(matrix):
    det = ((matrix[0][0])*(matrix[1][1]))-((matrix[0][1])*(matrix[1][0]))
    return det

def determinant(matrix):
    n = len(matrix)

    if len(matrix[0]) != len(matrix[-1]):
        return None
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return ((matrix[0][0])*(matrix[1][1]))-((matrix[0][-1])*(matrix[1][0]))
    
    if n == 3:
        mat1= [[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
        mat2= [[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
        mat3= [[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
        final = matrix[0][0]*(by2matrix(mat1)) - matrix[0][1]*(by2matrix(mat2)) + matrix[0][2]*(by2matrix(mat3))
        return final
