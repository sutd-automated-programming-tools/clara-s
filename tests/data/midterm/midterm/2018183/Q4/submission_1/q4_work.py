import copy
def determinant(matrix):
    op = copy.deepcopy(matrix)
    rowsize = len(op)
    colsize = len(op[0])
    coltrue = True
    ans = 0
    for i in op:
        if len(i) == colsize:
            continue
        else:
            coltrue = False
            break
    if coltrue == True:
        if rowsize == 1:
            ans = op[0][0]
        elif rowsize == 2:
            ans = op[0][0]*op[1][1] - op[0][1]*op[1][0]
        elif rowsize == 3:
            det1 = op[0][0]*(op[1][1]*op[2][2] - op[1][2]*op[2][1])
            det2 = -op[0][1]*(op[1][0]*op[2][2] - op[1][2]*op[2][0])
            det3 = op[0][2]*(op[1][0]*op[2][1] - op[1][1]*op[2][0])
            ans = det1 + det2 + det3
        return ans
    elif coltrue == False:
        return None