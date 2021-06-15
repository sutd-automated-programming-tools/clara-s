def determinant(matrix):
    if len(matrix) <1 or len(matrix) >3:
        return None
    for i in range(len(matrix)):
#        print(matrix[i])
#        print(len(matrix[i]))
        if len(matrix[i]) != len(matrix):
            return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
        return det
    if len(matrix) == 3:
        part1 = matrix[0][0]* ((matrix[1][1]*matrix[2][2])
                - matrix[2][1]*matrix[1][2])
        part2 = matrix[0][1]* ((matrix[1][0]*matrix[2][2])
                - matrix[2][0]*matrix[1][2])
        part3 = matrix[0][2]* ((matrix[1][0]*matrix[2][1])
                - matrix[2][0]*matrix[1][1])
        #print(part2)
        det = part1-part2+part3
        return det