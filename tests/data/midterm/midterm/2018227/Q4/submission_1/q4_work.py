def determinant(matrix):
    column=len(matrix[0])
    row=len(matrix)
    if row!=column:
        return None
    elif row == 1:
        return matrix[0][0]
    elif row ==2:
        det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
        return det
    else:
        deta=matrix[0][0] * ((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1]))
        detb=matrix[0][1] * ((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0]))
        detc=matrix[0][2] * ((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0]))
        return deta - detb +detc