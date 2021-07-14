def determinant_n1(matrix_n1):
    return matrix_n1[0][0]
    
def determinant_n2(matrix_n2):
    ad = matrix_n2[0][0] * matrix_n2[1][1]
    bc = matrix_n2[0][1] * matrix_n2[1][0]
    return ad-bc

def determinant_n3(matrix_n3):
    a = matrix_n3[0][0]
    b = matrix_n3[0][1]
    c = matrix_n3[0][2]
    d = matrix_n3[1][0]
    e = matrix_n3[1][1]
    f = matrix_n3[1][2]
    g = matrix_n3[2][0]
    h = matrix_n3[2][1]
    i = matrix_n3[2][2]
    part1 = a*((e*i)-(f*h))
    #print(part1)
    part2 = b*((d*i)-(f*g))
    #print(part2)
    part3 = c*((d*h)-(e*g))
    #print(part3)
    return part1-part2+part3

def determinant(matrix):
    for j in matrix:
        if len(j) != len(matrix):
            return None
        exit
    if len(matrix) == 1:
        n1 = determinant_n1(matrix)
        return n1
        exit
    elif len(matrix) == 2:
        n2 = determinant_n2(matrix)
        return n2
        exit
    else:
        n3 = determinant_n3(matrix)
        return n3
        exit