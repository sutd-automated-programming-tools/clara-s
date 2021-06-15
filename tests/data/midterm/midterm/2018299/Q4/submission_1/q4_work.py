def determinant(matrix):
    def determinant(matrix):
    for i in matrix:
        for j in matrix:
            if len(i) == len(j) == 2:
                det = i[0]*j[1] - i[1]*j[0]
        return det
    for i in matrix:
        for j in matrix:
            for k in matrix:
                if len(i) == len(j) == len(k) == 3:
                    det = i[0]*((j[1]*k[2])-(k[1]*j[2])) - j[0]*((i[1]*k[1])-(k[1]*i[2])) + k[0]*((i[1]*j[2])-(j[1]*i[2]))
            return det
    for i in matrix:
        if len(i) == 1:
            det = i
    return det
            