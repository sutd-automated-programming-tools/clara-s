def cofactor_matrix(matrix, row, col):
    matrix = matrix.copy()
    matrix.pop(row)
    matrix = list(zip(*matrix))
    matrix.pop(col)
    matrix = list(zip(*matrix))
    
    return matrix

def dim(matrix):
    return len(matrix), len(matrix[0])

def det2x2(matrix):
    assert dim(matrix) == (2, 2)
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

def determinant(matrix):
    # base cases
    matdim = dim(matrix)
    if matdim[0] != matdim[1]:
        return None
    
    if dim(matrix) == (1, 1):
        return matrix[0][0]
    
    if dim(matrix) == (2, 2):
        return det2x2(matrix)
    
    # can go on one but...
    if dim(matrix) == (3, 3):
        det = 0
        for i, cofactor in enumerate(matrix[0]):
            multiplier = 1 if i % 2 == 0 else -1
            det += multiplier * cofactor * determinant(
                cofactor_matrix(matrix, 0, i)
            )
        return det
    
    # fell thru
    return None