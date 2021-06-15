def determinant(matrix):
    a = 0
    while a < len(matrix):
        if len(matrix[a]) != len(matrix):
            return None
            break
        a += 1
    if len(matrix) == 1:
        detM = matrix[0][0]
    elif len(matrix) == 2:
        detM = ( (matrix[0][0])*(matrix[1][1]) )-( (matrix[0][1])*(matrix[1][0]) )
    return detM            

            