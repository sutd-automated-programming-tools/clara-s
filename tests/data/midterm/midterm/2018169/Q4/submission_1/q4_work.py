def determinant(matrix):
    for i in matrix:
        while i <= 3 and i >=1:
            if i != len(matrix):
                return None
            if i == 1:
                return i
            elif i == 2:
                return matrix[0][0] + matrix[1][1]
            elif i == 3:
                return (matrix[0][0])*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]) - (matrix[0][1])*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]) + (matrix[0][2])*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])