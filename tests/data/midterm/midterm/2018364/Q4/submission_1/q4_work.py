def determinant(matrix):
    ans = 0.0
    n = len(matrix)
    if len(matrix)!= len(matrix[0]):
        return (None)
    elif n == 1:
        ans = matrix[0][0]
    elif n == 2:
        ans = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    elif n == 3:
        a1 = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        a2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        a3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        ans = a1 - a2 + a3
    return (ans)
