def determinant(m):
    if len(m) != len(m[0]):
        return None
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m [1][0]
    elif len(m) == 3:
        value1 = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        value2 = m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        value3 = m[0][2] * (m[1][0] * m[2][1] - m[2][0] * m[1][1])
        return value1 - value2 + value3