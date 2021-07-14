import copy

def determinant(matrix):
    
    if(len(matrix)<1 or len(matrix)>3):
        return None
    
    for i in range(len(matrix)):
        if(len(matrix)!=len(matrix[i])):
            return None
    
    if(len(matrix)==1):
        return matrix[0][0]
    
    if(len(matrix)==2):
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    
    det = 0
    for i in range(3):
        intermediate = [[matrix[1][j] for j in range(3)], [matrix[2][j] for j in range(3)]]
        del intermediate[0][i]
        del intermediate[1][i]
        det += matrix[0][i] * (-1)**i * determinant(intermediate)
    
    return det