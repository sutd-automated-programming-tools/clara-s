def determinant(matrix):
    list = []
    for i in matrix:
        n = len(i)
    for i in range(0,len(matrix)):
        list.append(len(matrix[i]))
    if n == 1:
        for i in matrix:
            for x in i:
                det = x
    elif n ==2:
        if list[0] != list[1]:
            return
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            det = (a*d) - b*c
        
    elif n == 3:
        if list[0] != list[1]:
            return
        else:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            det = a*(e*i - f*h) - b*(d*i - g*f) + c*(d*h - g*e)
        
    
            
    return det