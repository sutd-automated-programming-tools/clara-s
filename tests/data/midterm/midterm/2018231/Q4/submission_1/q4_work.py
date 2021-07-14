def determinant(matrix):
        if len(matrix[0]) != len(matrix):
            return None
        if len(matrix) == 1:
            ans1 = matrix[0][0]
            return ans1
        elif len(matrix) == 2:
            ans2 = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
            return ans2
        elif len(matrix) == 3:
            lst = matrix[0]
            det1 = (matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1])
            det2 = (matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])
            det3 = (matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])
            ans = (lst[0] * det1) - (lst[1] * det2) + (lst[2] * det3)
            return ans

print(determinant([[-5, -4], [-2, -3]]))