def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        try:
            output = det_2(matrix)
        except:
            output = None
    elif len(matrix) == 3:
        try:
            det = 0
            for x, item in enumerate(matrix[0][:]):
                cofactor_extra = matrix[1:]
                cofactor = []
                for row in cofactor_extra:
                    if x == 0:
                        cofactor.append(row[1:])
                    elif x == 1:
                        cofactor.append([row[0], row[2]])
                    elif x == 2:
                        cofactor.append(row[:2])
                if x == 1:
                    det -= item * det_2(cofactor)
                else:
                    det += item * det_2(cofactor)
            output = det
        except:
            output = None
    else:
        output = None
    return output

def det_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]