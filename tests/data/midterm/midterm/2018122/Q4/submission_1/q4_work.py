
def determinant(matrix):
    if not(len(matrix) == len(matrix[0])):
        return None
    elif len(matrix[0]) ==1:
        ans1 = matrix[0][0]
        return ans1
    elif len(matrix[0]) == 2:
        ans2 = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
        return ans2
    elif len(matrix[0]) == 3:
        a = matrix[0][0]
        a_det = (matrix[1][1]*matrix[2][2]) - (matrix[1][2] * matrix[2][1] )
        b = matrix[1][0]
        b_det = (matrix[0][1]*matrix[2][2]) - (matrix[0][2] * matrix[2][1] )
        c = matrix[2][0]
        c_det = (matrix[0][1]*matrix[1][2]) - (matrix[0][2] * matrix[1][1] )
        ans3 = (a * a_det) - (b * b_det) + (c * c_det)
        return ans3