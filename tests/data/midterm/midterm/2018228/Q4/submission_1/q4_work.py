def determinant(matrix):
    m = len(matrix)
    n = len(matrix[0])
    m_con = 1 <= m <= 3
    n_con = 1 <= n <= 3
    if m == n and m_con and n_con:
        if n == 1:
            det = matrix[0][0]
        elif n == 2:
            val1 = matrix[0][0]*matrix[1][1]
            val2 = matrix[0][1]*matrix[1][0]
            det = val1 - val2
        else:
            row1 = matrix[0]
            det1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
            det2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
            det3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
            resdet = row1[0]*det1 - row1[1]*det2 + row1[2]*det3
            return resdet
    else:
        return None