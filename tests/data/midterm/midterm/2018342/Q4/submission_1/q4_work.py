def n1(ls):
    return ls[0][0]

def n2(ls):
    return ls[0][0] * ls[1][1] - ls[0][1] * ls[1][1]

def n3(ls):
    part1 = ls[0][0] * n2([ls[1][1:], ls[2][1:]])
    part2 = ls[0][1] * n2([[ls[1][0],ls[1][2]],[ls[2][0],ls[2][2]])
    part3 = ls[0][2] * n2([[ls[1][0],ls[1][1]],[ls[2][0],ls[2][1]]])

    return part1 - part2 + part3

def determinant(matrix):

    n = len(matrix)
    for i in range(n):
        if len(matrix[i]) != n:
            return None
    if n == 1:
        return n1(matrix)
    elif n == 2:
        return n2(matrix)
    elif n == 3:
        return n3(matrix)