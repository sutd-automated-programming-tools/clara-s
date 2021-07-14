def determinant(matrix):
    n1 = len(matrix)
    n2 = len(matrix[0])
    if n1 != n2:
        return None
    else:
        if n1 == 1:
            ans = matrix[0][0]
            return ans
        if n1 == 2:
            ans = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
            return ans
        if n1 == 3:
            row1 = matrix[0]
            row2 = matrix[1]
            row3 = matrix[2]
            ans1 = row1[0]*((row2[1]*row3[2]) - (row3[1]*row2[2]))
            ans2 = -row1[1]*((row2[0]*row3[2]) - (row3[0]*row2[2]))
            ans3 = row1[2]*((row2[0]*row3[1]) - (row3[0]*row2[1]))
            ans = ans1 + ans2 + ans3
            return ans