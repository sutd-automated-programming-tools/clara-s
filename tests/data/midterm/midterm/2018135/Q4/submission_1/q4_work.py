def determinant(matrix):
    n = len(matrix)
    if n == 1:
        ans = matrix[0][0]
    elif n == 2:
        ans = int(matrix[0][0])*int(matrix[1][1])-int(matrix[0][1])*int(matrix[1][0])
    elif n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        ans = a*(e*i-h*f)-b*(d*i-g*f)+c*(d*h-e*g)
    else:
        return None
    return ans