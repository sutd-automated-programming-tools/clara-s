def determinant(matrix):
    row = len(matrix)
    print(matrix[0])
    col = len(matrix[0])
    n = row
    if n < 1 or n > 3 and row != col:
        return None
    if n == 1:
        return matrix[0][0]
    if n == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return (a*d - b*c)
    if n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        det = a*determinant([matrix[1][1:],matrix[2][1:]]) + \
              b*determinant([matrix[1][0]+matrix[1][2],matrix[2][0]+matrix[2][2]]) + \
              c*determinant([matrix[1][:1],matrix[2][:1]])
        return det