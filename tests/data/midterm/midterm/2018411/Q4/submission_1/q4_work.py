def determinant(matrix):
    if len(matrix) == len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == len(matrix[0]) == len(matrix[1]) == 2:
        ans = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return ans
    elif len(matrix) == len(matrix[0]) == len(matrix[1]) == len(matrix[2]) == 3:
        a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
        d, e, f = matrix[1][0], matrix[1][1], matrix[1][2]
        g, h, i = matrix[2][0], matrix[2][1], matrix[2][2]
        answer = (a*(e*i - h*f)) - (b*(d*i - g*f)) + (c*(d*h - g*e))
        return answer
    else:
        return None