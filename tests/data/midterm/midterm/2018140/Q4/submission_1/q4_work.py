def determinant(matrix):
    def det2(m):
        a,b = m[0]
        c,d = m[1]
        return a*d-b*c
    
    n = len(matrix)
    m = len(matrix[0])
    if n != m or not 1 <= n <= 3:
        print('invalid')
        return None
    elif n == 1:
        return matrix[0][0]
    elif n == 2:
        print(matrix)
        print('2x2')
        return det2(matrix)
    else:
        print(matrix)
        print('3x3')
        a,b,c = matrix[0]
        d,e,f = matrix[1]
        g,h,i = matrix[2]
        return a*det2([[e,f],[h,i]]) -b*det2([[d,f,],[g,i]]) + c*det2([[d,e],[g,h]])