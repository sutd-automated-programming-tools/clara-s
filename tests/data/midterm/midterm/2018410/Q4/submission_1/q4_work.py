def determinant(matrix):
    if len(matrix) == 1:
        if len(matrix[0]) == 1:
            return matrix[0][0]
    
    if len(matrix) == 2:
        if len(matrix[0]) == 2 and len(matrix[1]) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) == 3:
        if len(matrix[0]) == 3 and len(matrix[1]) == 3 and len(matrix[2]) == 3:
            det1 = determinant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]])
            det2 = determinant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]])
            det3 = determinant([[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]])
            return matrix[0][0]*det1 - matrix[0][1] * det2 + matrix[0][2] * det3
print(determinant([[0,3,5],[5,5,2],[3,4,3]]))
