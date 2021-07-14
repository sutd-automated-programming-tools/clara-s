def determinant(matrix, mul):
width = len(matrix)
 if width == 1:
    return mul * matrix[0][0]
 else:
    sign = -1
    sum = 0
    for i in range(width):
        m = []
        for j in range(1, width):
            buff = []
            for k in range(width):
                if k != i:
                    buff.append(matrix[j][k])
            m.append(buff)
        sign *= -1
        sum += mul * determinant(m, sign * matrix[0][i])
    return sum