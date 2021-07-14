def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        ans1 = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
        return ans1
    if len(matrix) == 3:
        firstpart = (matrix[0][0])*((matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2]))
        secondpart = (matrix[0][1])*((matrix[1][0]*matrix[2][2])-(matrix[2][0]*matrix[1][2]))
        thirdpart = (matrix[0][2])*((matrix[1][0]*matrix[2][1])-(matrix[2][0]*matrix[1][1]))
        return firstpart - secondpart + thirdpart
    else: 
        return None