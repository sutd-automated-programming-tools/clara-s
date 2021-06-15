def determinant(m):

    for row in m:
        if len(m) != len(row):
            return None
        if len(m) == 1:
            return row[0]
        else:
            if len(m)==2:
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]
            elif len(m)==3:
                return m[0][0]*(m[1][1] * m[2][2] - m[1][2] * m[2][1])-m[0][1]*(m[1][0] * m[2][2] - m[1][2] * m[2][0])+m[0][2]*(m[1][0] * m[2][1] - m[1][1] * m[2][0])