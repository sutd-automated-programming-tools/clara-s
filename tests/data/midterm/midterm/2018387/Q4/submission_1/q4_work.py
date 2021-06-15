def determinant(lst):
    det = 0.0
    if len(lst) == 1:
        #do stuff
        det=lst[0][0]
        return det
    if len(lst) == 2:
        if len(lst[0]) != 2:
            det = None
            return det
        det = (lst[0][0])*(lst[1][1])-(lst[1][0])*(lst[0][1])
        return det
    if len(lst) == 3:
        if len(lst[0]) != 3:
            det = None
            return det
        a = lst[0][0]
        b = lst[0][1]
        c = lst[0][2]
        d = lst[1][0]
        e = lst[1][1]
        f = lst[1][2]
        g = lst[2][0]
        h = lst[2][1]
        i = lst[2][2]
        det = (a*(c*i-h*f))-(b*(d*i-g*f))+(c*(d*h-g*c))
        return det