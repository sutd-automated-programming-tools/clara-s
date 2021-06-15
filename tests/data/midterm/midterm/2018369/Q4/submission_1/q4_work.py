def determinant(matrix):
	pass
def matrix_2by2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return det


def determinant(matrix):
    m, n = (len(matrix), len(matrix[0]))    #checking dimensions
    if m != n or m > 3 or m < 1:
        return None
    else:
        if m == 1:
            det = matrix[0][0]
        elif m == 2:
            det = matrix_2by2(matrix)
        elif m == 3:
            row1, row2, row3 = matrix[0], matrix[1], matrix[2]
            a, b, c = row1[0], row1[1], row1[2]
            d, e, f = row2[0], row2[1], row2[2]
            g, h, i = row3[0], row3[1], row3[2]
            det = a * matrix_2by2([[e, f], [h, i]]) - b * matrix_2by2([[d, f], [g, i]]) + c * matrix_2by2([[d, e], [g, h]])
        return det