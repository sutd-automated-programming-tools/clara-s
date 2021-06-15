def determinant(matrix):
    if not(len(matrix) <= 3 and len(matrix) >= 1):
        return None
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return None
    
    det = 0
    if len(matrix) == 1:
        det = matrix[0]
        
    if len(matrix) == 2:
        det = matrix[0][0]*matrix[1][1] - (matrix[0][1]*matrix[1][0])
        
    if len(matrix) ==3:
        first_matrix = (matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2])
        second_matrix = (matrix[1][0]*matrix[2][2])-(matrix[2][0]*matrix[1][2])
        third_matrix = (matrix[1][0]*matrix[2][1])-(matrix[2][0]*matrix[1][1])
        det = matrix[0][0]*first_matrix - matrix[0][1]*second_matrix + matrix[0][2]*third_matrix
        
    return det