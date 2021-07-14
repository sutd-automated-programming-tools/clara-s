
def determinant(matrix):
    n = len(matrix)
    lst = []
    for k in range(n):
        length = len(matrix[k])
        lst.append(length)            #lst with [len1 , len2 , len3]
    if n == 1:
        det = matrix[0][0]
    elif n == 2:
        if lst[0] != lst[1]:
            return None
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        det = a * d - b * c
    elif n == 3:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        d = matrix[1][0]
        e = matrix[1][1]
        f = matrix[1][2]
        g = matrix[2][0]
        h = matrix[2][1]
        i = matrix[2][2]
        mat1 = [[e,f] , [h,i]]
        mat2 = [[d,f] , [g,i]]
        mat3 = [[d,e] , [g,h]]
        det = a*determinant(mat1) - b*determinant(mat2) + c*determinant(mat3)
            
    return det