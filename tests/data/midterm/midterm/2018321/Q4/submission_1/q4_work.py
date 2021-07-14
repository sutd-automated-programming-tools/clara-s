def determinant(matrix):

    if len(matrix) == 1:
        for i in matrix:
            for a in i:
                return a
            
    elif len(matrix) == 2:
        c = []
        d = []
        for i in matrix:
            a = (i[0])
            b = i[1]
            c.append(a)
            d.append(b)
            d = d [::-1]
            e = c + d
            print (e)