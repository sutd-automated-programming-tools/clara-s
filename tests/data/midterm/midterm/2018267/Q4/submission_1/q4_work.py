import copy


def matrix2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]


def determinant(matrix):
    det = None
    length = len(matrix)
    if length not in (1,2,3):
        return None
    innerlength = len(matrix[0])
    if length != innerlength:
        return None
    if length == 2:
        if length != len(matrix[1]):
            return None
    if length == 3:
        if length != len(matrix[2]):
            return None
    
    if length == 1:
        det = matrix[0][0]
        
    elif length == 2:
        det = matrix2(matrix)
    elif length == 3:
        thematrix = copy.deepcopy(matrix)
        del thematrix[1][1]
        del thematrix[2][1]
        mat1 = [matrix[1][1:],matrix[2][1:]]
        mat2 = [thematrix[1][:],thematrix[2][:]]
        mat3 = [matrix[1][:2],matrix[2][:2]]
        det = matrix[0][0]*matrix2(mat1) - matrix[0][1]*matrix2(mat2) + matrix[0][2]*matrix2(mat3)
    else:
        return None
    
    
    return det