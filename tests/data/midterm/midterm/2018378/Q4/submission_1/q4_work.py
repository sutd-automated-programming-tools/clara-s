def det(a,b,c,d):
    return a*d-b*c

def determinant(matrix):
    for row in matrix:
        if len(row) != len(matrix) or len(row)>3 or len(row)<1:
            return None
    if len(matrix)==1:
        return matrix[0][0]
    if len(matrix)==2:
        return det(matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1])
    if len(matrix)==3:
        return matrix[0][0]*det(matrix[1][1],matrix[1][2],matrix[2][1],matrix[2][2]) - matrix[0][1]*det(matrix[1][0],matrix[1][2],matrix[2][0],matrix[2][2]) + matrix[0][2]*det(matrix[1][0],matrix[1][1],matrix[2][0],matrix[2][1])
    else:
        return None