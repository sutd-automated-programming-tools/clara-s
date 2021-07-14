def find_determinant(matrix):
    y_len = int(len(matrix))
    x_len = int(len(matrix[0]))
    if x_len != y_len:
        return None
    elif x_len not in range(1,4):
        return None
    else:
        if x_len == 1:
            det = matrix[0]
            return det
        if x_len == 2:
            det = (matrix[0][0]*matrix[1][1])+(matrix[0][1]*matrix[1][0])
            return det
        if x_len == 3:
            a = matrix[0][0]
            b=matrix[0][1]
            c=matrix[0][2]
            d=martix[1][0]
            e=matrix[1][1]
            f=matrix[1][2]
            g=matrix[2][0]
            h=matrix[2][1]
            i = matrix[2][2]
            det1= (e*i)-(h*f)
            det2 = (d*i)-(g*f)
            det3 = (d*h)-(g*e)
            det = (a*det1)-(b*det2)+(c*det3)
            return det