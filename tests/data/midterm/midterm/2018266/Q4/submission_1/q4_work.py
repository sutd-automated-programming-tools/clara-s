def determinant2(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det2 = a*d - b*c
    return det2

def determinant3(matrix):
    first = [matrix[1][1:], matrix[2][1:]]
    second= [matrix[1][::2], matrix[2][::2]]
    third = [matrix[1][:2], matrix[2][:2]]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    det3 = a*determinant2(first) - b*determinant2(second) + c*determinant2(third)
    return det3

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        if len(matrix[0]) == len(matrix[1]):
            return determinant2(matrix)
        else:
            return None
    elif len(matrix) == 3:
        if len(matrix[0]) == len(matrix[1]) and len(matrix[1]) == len(matrix[2]):
            return determinant3(matrix)
        else:
            return None
    else:
        return None