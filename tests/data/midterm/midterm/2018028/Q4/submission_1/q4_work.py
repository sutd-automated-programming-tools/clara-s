def determinant(matrix):
    for i in matrix:
        print(i)
        if len(i) == 1:
            return i[0]
        if len(i) == 2:

            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            ans = a*d - b*c
            return ans
        
        if len(i) == 3:
            a =matrix[0][0]
            b =matrix[0][1]
            c =matrix[0][2]
            d = matrix[1][0]
            e = matrix[1][1]
            f = matrix[1][2]
            g = matrix[2][0]
            h = matrix[2][1]
            i = matrix[2][2]
            ans1 = e*i - h*f
            ans2 = d*i - f*g
            ans3 = d*h - e*g
            ansf = a*ans1 - b*ans2 + c*ans3
            return ansf 
        
        if len(i[0]) != len(i[1]):
            return None