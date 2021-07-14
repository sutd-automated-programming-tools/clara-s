def determinant(matrix):
    m = matrix
    if len(m[0]) == 1 and len(m) == 1:
        for element in m[0]: #for n = 1
            if type(element) == int:
                return element
    elif len(m[0]) == 4 and len(m[0][0]) ==2 and len(m[0][1]) ==2:
        a = m[0][0][0]
        b = m[0][0][1]
        c = m[0][1][0]
        d = m[0][1][1]
        det = a*b - c*d
        return det
    elif len(m[0]) ==9 and len(m[0][0]) ==3 and len(m[0][1]) == 3 and len(m[0][2]) == 3:
        a = m[0][0][0]
        b = m[0][0][1]
        c = m[0][0][2]
        d = m[0][1][0]
        e = m[0][1][1]
        f = m[0][1][2]
        g = m[0][2][0]
        h = m[0][2][1]
        i = m[0][2][2]
        det = a*(determinant([[e,f],[h,i]]) - b*(determinant([[d,f],[g,i]]) + c*(determinant([[d,e],[g,h]])
        return det