def determinant(m):
    if len(m) != len(m[0]):
        return None
    if len(m) < 1 or len(m) > 3:
        return None
    if len(m) ==1:
        return m[0][0]
    if len(m) == 2:
        return (m[0][0]*m[1][1] - m[0][1]*m[1][0])
    else:
        one= m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
        two= m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
        three= m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
        output = one - two + three
        return output