def determinant(matrix):
    length = len(matrix)
    leng = len(matrix[0])
    if length < 1 or length > 3 or leng != length:
        return None
    elif length == 1:
        det = matrix[0][0]
        return det
    elif length ==2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix [1][0]
        return det 
    elif length == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        det = a * (e * i - h * f) - b *(d * i - g * f) + c *(d * h -g *e)
        return det