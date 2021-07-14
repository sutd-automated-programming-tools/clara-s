def determinant(matrix):
    n = len(matrix)
    for row in matrix:
        j = len(row)
        if j != n:
            return None
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if n ==3:
        a = matrix[0][0]
        mat1 = [matrix[1][1:3],matrix[2][1:3]]
        detmat1 = mat1[0][0] * mat1[1][1] - mat1[0][1] * mat1[1][0]
        
        b = matrix[0][1]
        mat2 = [[matrix[1][0], matrix[1][2]],[matrix[2][0], matrix[2][2]]]
        detmat2 = mat2[0][0] * mat2[1][1] - mat2[0][1] * mat2[1][0]
        
        c = matrix[0][2]
        mat3 = [matrix[1][0:2],matrix[2][0:2]]
        detmat3 = mat3[0][0] * mat3[1][1] - mat3[0][1] * mat3[1][0]
        
        
        return a * detmat1 - b * detmat2 + c * detmat3