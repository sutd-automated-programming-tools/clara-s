def det(m):
    result = (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    return result
    
def determinant(matrix):
    if len(matrix) == 1:
        if len(matrix) == 1:
            return matrix[0][0]
        else:
            return None
    elif len(matrix) == 2:
        if len(matrix[0]) == 2 and len(matrix[1]) == 2:
            return det(matrix)
        else:
            print(len(matrix[1]))
            return None
    elif len(matrix) == 3:
        if len(matrix[0]) == 3 and len(matrix[1]) == 3 and len(matrix[2]) == 3:
            m = matrix
            a = [[m[1][1],m[1][2]],[m[2][1],m[2][2]]]
            b = [[m[1][0],m[1][2]],[m[2][0],m[2][2]]]
            c = [[m[1][0],m[1][1]],[m[2][0],m[2][1]]]
            result = (m[0][0]*det(a)) - (m[0][1]*det(b)) + (m[0][2]*det(c))
            return result
        else:
            return None