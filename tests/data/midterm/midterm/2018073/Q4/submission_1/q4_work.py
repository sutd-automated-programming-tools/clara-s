def det_matrix_22(x):
    return x[0][0] * x[1][1] - x[0][1] * x[1][0]

def determinant(x):
    length = len(x)
    side_length = len(x[0])
    if length != side_length:
        return None
    elif length == 1:
        return x[0][0]
    elif length == 2:
        return det_matrix_22(x)
    elif length == 3:
        new_x = []
        new_x_row1 = []
        new_x_row2 = []
        new_x_row1.append(x[1][1])
        new_x_row1.append(x[1][2])
        new_x_row2.append(x[2][1])
        new_x_row2.append(x[2][2])
        new_x.append(new_x_row1)
        new_x.append(new_x_row2)

        new_x2 = []
        new_x2_row1 = []
        new_x2_row2 = []
        new_x2_row1.append(x[1][0])
        new_x2_row1.append(x[1][2])
        new_x2_row2.append(x[2][0])
        new_x2_row2.append(x[2][2])
        new_x2.append(new_x2_row1)
        new_x2.append(new_x2_row2)

        new_x3 = []
        new_x3_row1 = []
        new_x3_row2 = []
        new_x3_row1.append(x[1][0])
        new_x3_row1.append(x[1][1])
        new_x3_row2.append(x[2][0])
        new_x3_row2.append(x[2][1])
        new_x3.append(new_x3_row1)
        new_x3.append(new_x3_row2)

        det1 = x[0][0] * det_matrix_22(new_x)
        det2 = x[0][1] * det_matrix_22(new_x2)
        det3 = x[0][2] * det_matrix_22(new_x3)

        return det1 - det2 + det3