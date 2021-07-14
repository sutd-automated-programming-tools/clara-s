def determinant(matrix):
    def det_2(ma):
        return ma[0][0] * ma[1][1] - ma[0][1] * ma[1][0]

    if len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return det_2(matrix)
    elif len(matrix) == 3:
        m = matrix
        a_lst = [[m[1][1], m[1][2]], [m[2][1], m[2][2]]]
        b_lst = [[m[0][1], m[0][2]], [m[2][1], m[2][2]]]
        c_lst = [[m[0][1], m[0][2]], [m[1][1], m[1][2]]]
        return matrix[0][0] * det_2(a_lst) - matrix[1][0] * det_2(b_lst) + matrix[2][0] * det_2(c_lst)