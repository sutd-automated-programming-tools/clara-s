def determinant(matrix):
    def dett(mat):
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        
    if len(matrix) > 3:
        return None
    elif len(matrix) ==1 and type(matrix[0]) != list:
        det = matrix[0]
    elif len(matrix) ==1 and type(matrix[0]) == list and len(matrix[0]) == 1:
        det = matrix[0][0]
    elif len(matrix) ==2:
        if len(matrix[0]) != len(matrix[1]) or len(matrix[0]) != 2:
            return None
        else:
            det = dett(matrix)
            
    elif len(matrix) ==3:
        if len(matrix[0]) != len(matrix[1]) or len(matrix[0]) != len(matrix[2]) or len(matrix[0]) != 3:
            return None
        else:
            det1 = matrix[0][0]*dett([[matrix[1][1], matrix[1][2]],[matrix[2][1], matrix[2][2]]])

            det2 = matrix[0][1]*dett([[matrix[1][0], matrix[1][2]],[matrix[2][0], matrix[2][2]]])

            det3 = matrix[0][2]*dett([[matrix[1][0], matrix[1][1]],[matrix[2][0], matrix[2][1]]])
            det = det1 - det2 + det3
    return det