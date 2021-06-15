def determinant(matrix):
    for i in matrix:
        i = i[:]
    if len(matrix) == 1:
        return matrix[0,0]
    if len(matrix) == 2:
        if len(matrix[0]) == len(matrix[1]):
            return (matrix[0,0])*(matrix[1,1]) - (matrix[0,1])*(matrix[1,0])
        else:
            return None
    if len(matrix) == 3:
        det_efhi = (matrix[1,1])*(matrix[2,2]) - (matrix[1,2])*(matrix[2,1])
        det_dfgi = (matrix[1,0])*(matrix[2,2]) - (matrix[1,2])*(matrix[2,0])
        det_degh = (matrix[1,0])*(matrix[2,1]) - (matrix[1,1])*(matrix[2,0])
        return (matrix[0,0])*(det_efhi) - (matrix[0,1])*(det_dfgi) + (matrix[0,2])*(det_degh)
            
        