def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None

    
    if len(matrix[0])==1:
        det = matrix[0][0]
        
    elif len(matrix[0])==2:
        det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])

    elif len(matrix[0]) ==3:
        det = (matrix[0][0]*((matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1]))) - (matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0]))) + (matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])))
    
    return det
    