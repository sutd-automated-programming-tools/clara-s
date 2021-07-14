def determinant(matrix):
    col_len = len(matrix)
    for i in matrix:
        row_len = len(i)
        if col_len < 1 and row_len < 1:
             return None
        if col_len > 3 and row_len > 3:
            return None
        if col_len == 1 and row_len == 1:
              return i[0]
        if col_len == 2 and row_len == 2:
            ad = matrix[0][0] * matrix[1][1]
            bc = matrix[0][1] * matrix[1][0]
            return ad - bc
        if col_len == 3 and row_len == 3:
            a1 = matrix[0][0]
            a2 = matrix[0][1]
            a3 = matrix[0][2]
            ad1 = matrix[1][1] * matrix[2][2]
            bc1 = matrix[1][2] * matrix[2][1]        
            ad2 = matrix[1][0] * matrix[2][2]
            bc2 = matrix[2][0] * matrix[1][2]
            ad3 = matrix[1][0] * matrix[2][1]
            bc3 = matrix[2][0] * matrix[1][1]
            deter = a1* (ad1 - bc1) - a2*(ad2 - bc2) + a3*(ad3 - bc3)
            return deter