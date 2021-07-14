def determinant(matrix):
    n = 0
    n1 = 0
    for counter in matrix:
        for counter2 in counter:
            n1 +=1
        n +=1
    n1 = n1 / n
    #print(n , n1)
    if n < 1 or n >3 or n1 != n:
        return None
    else:
        if n == 2:
            det2 = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            return det2
        elif n == 1:
            return matrix[0][0]
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
            det3 = (a*(e*i-f*h))-(b*(d*i-f*g))+(c*(d*h-e*g))
            return det3