def x1m(matrix):
    ans = matrix[0][0]
    return ans

def x2m(matrix):
    ans = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    return ans

def x3m(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    m1 = [[e,f],[h,i]]
    m2 = [[d,f],[g,i]]
    m3 = [[d,e],[g,h]]
    ans = (a*x2m(m1))-(b*x2m(m2))+(c*x2m(m3))
    return ans

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    else:
        if len(matrix) == 1:
            ans = x1m(matrix)
        elif len(matrix) == 2:
            ans = x2m(matrix)
        elif len(matrix) == 3:
            ans = x3m(matrix)
    return ans