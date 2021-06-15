def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3  or len(matrix[0]) < 1  or len(matrix[0]) > 3:
        return None
    if len(matrix) > 1:
        for i in range(0,len(matrix)-1):
            if len(matrix[i]) != len(matrix[i+1]):
                return None
    if len(matrix) == 1 and len(matrix[0]) != 1:
        return None
    def twoxtwodet(twomatrix):
        return twomatrix[0][0]*twomatrix[1][1] - twomatrix[0][1]* twomatrix[1][0]
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return twoxtwodet(matrix)
    elif len(matrix) == 3:
        amatrix = [[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
        bmatrix = [[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
        cmatrix = [[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
        print(amatrix,bmatrix,cmatrix)
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        return a*twoxtwodet(amatrix) - b*twoxtwodet(bmatrix) + c*twoxtwodet(cmatrix)
