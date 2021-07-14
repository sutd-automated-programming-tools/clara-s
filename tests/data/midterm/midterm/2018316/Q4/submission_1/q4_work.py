def determinant(m):
    if len(m) != len(m[0]) or len(m) > 3:
        return None
    elif len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return(m[0][0] * m[1][1] - m[0][1] * m[1][0])
    det = m[0][0] * determinant([[m[1][1],m[1][2]],[m[2][1],m[2][2]]]) - m[1][0] * determinant([[m[0][1],m[0][2]],[m[2][1],m[2][2]]]) + m[2][0] * determinant([[m[0][1],m[0][2]],[m[1][1],m[1][2]]])
    return(det)