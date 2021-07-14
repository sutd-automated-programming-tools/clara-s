def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        if len(matrix[0])!=len(matrix[1]):
            return None
        else:
            return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    elif len(matrix)==3:
        if len(matrix[0])!=len(matrix[1]) or len(matrix[1])!=len(matrix[2]) or len(matrix[0])!=len(matrix[2]):
            return None
        else:
            part1=(matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])
            print(part1)
            part2=(matrix[1][0]*matrix[2][2])-(matrix[2][0]*matrix[1][2])
            print(part2)
            part3=(matrix[1][0]*matrix[2][1])-(matrix[2][0]*matrix[1][1])
            print(part3)
            return ((matrix[0][0]*part1)-(matrix[0][1]*part2)+(matrix[0][2]*part3))
    else:
        return None