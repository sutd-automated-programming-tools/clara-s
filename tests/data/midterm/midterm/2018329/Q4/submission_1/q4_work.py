
def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:#if m is 1x1
        return matrix[0][0]
    elif len(matrix) == 2:
        return  (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
    elif len(matrix) == 3:
        first = matrix[0][0] * det([matrix[1][1:],matrix[2][1:]])
        second = matrix[0][1] * det([matrix[1][::2],matrix[2][::2]])
        third = matrix[0][2] * det([matrix[1][:-1],matrix[2][:-1]])
        return (first - second + third)