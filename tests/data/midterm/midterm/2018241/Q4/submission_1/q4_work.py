def determinant(matrix):
    no_rows = len(matrix)
    no_columns = len(matrix[0])
    if no_rows != no_columns:
        return None
    if no_rows < 1 or no_rows > 3 or no_columns < 1 or no_columns > 3:
        return None
    elif no_rows ==  1 and no_columns == 1:
        return matrix[0][0]
    elif no_rows == 2 and no_columns == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif no_rows == 3 and no_columns == 3:
        return matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])- matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+ matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    else:
        return None