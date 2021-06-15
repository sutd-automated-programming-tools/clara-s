def determinant(mat):
    for i in mat:
        if len(i) != len(mat):
            return None
    if len(mat) == 1:
        return mat[0][0]
    if len(mat)==2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    a = mat[0][0] * (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
    b = mat[0][1] * (mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
    c = mat[0][2] * (mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
    return a-b+c