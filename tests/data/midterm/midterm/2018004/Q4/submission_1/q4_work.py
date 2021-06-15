def determinant(matrix):
    if len(matrix[0]) != len(matrix) or len(matrix) > 3 or len(matrix) < 1:
        return None
    else:
        n = len(matrix)
        if n==1:
            return matrix[0][0]
        elif n==2:
            lees = []
            for i in range(2): 
                for j in range(2): 
                    lees.append(matrix[i][j]) 
            return lees[0] * lees[3] - lees[1] * lees[2]
        else:
            ls = []
            for i in range(3):
                for j in range(3):
                    ls.append(matrix[i][j])
            print(ls)
            return ls[0] * determinant([[ls[4], ls[5]], [ls[7], ls[8]]]) - ls[1] * determinant([[ls[3], ls[5]], [ls[6], ls[8]]]) + ls[2] * determinant([[ls[3], ls[4]], [ls[6], ls[7]]])