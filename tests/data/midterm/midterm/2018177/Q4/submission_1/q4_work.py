def determinant(matrix):
    while 1<=len(matrix)<=3:
        if not len(matrix) == len(matrix[0]):
            return None
        else:
            if len(matrix) == 1:
                ans = matrix[0][0]
                return ans
            elif len(matrix) == 2:
                part1 = matrix[0][0] * matrix[1][1]
                part2 = matrix[0][1] * matrix[1][0]
                ans = part1 - part2
                return ans
            elif len(matrix) == 3:
                list1 = [(matrix[1][1],matrix[1][2]),(matrix[2][1],matrix[2][2])]
                list2 = [(matrix[1][0],matrix[1][2]),(matrix[2][0],matrix[2][2])]
                list3 = [(matrix[1][0],matrix[1][1]),(matrix[2][0],matrix[2][1])]
                first = list1[0][0] * list1[1][1] - list1[0][1] * list1[1][0]
                second =list2[0][0] * list2[1][1] - list2[0][1] * list2[1][0]
                third = list3[0][0] * list3[1][1] - list3[0][1] * list3[1][0]
                ans2 = matrix[0][0]*first - matrix[0][1]*second + matrix[0][2]*third
                return ans2
