def ad_bc(matrix):
    ad = matrix[0][0]*matrix[1][1]
    bc = matrix[0][1]*matrix[1][0]
    return ad-bc

def determinant(matrix):
    if len(matrix) > 3 or len(matrix) < 1:
        return None
    for i in matrix:
#        print(i)
        if len(i) > 3 or len(i) < 1 or len(i) != len(matrix):
            return None
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return ad_bc(matrix)        
    if n == 3:
        first = [[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
        second = [[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
        third = [[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
        return matrix[0][0]*ad_bc(first) - matrix[0][1]*ad_bc(second) + matrix[0][2]*ad_bc(third)
