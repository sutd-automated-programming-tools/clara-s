def determinant(inp):
    oup = None
    if len(inp) == len(inp[0]) == 1:
        oup = inp[0][0]
    if len(inp) == len(inp[0]) == 2:
        det = inp[0][0]*inp[1][1]-inp[0][1]*inp[1][0]
        oup = det
    if len(inp) == len(inp[0]) == 3:
        det1 = inp[0][0]*(inp[1][1]*inp[2][2]-inp[1][2]*inp[2][1])
        det2 = inp[0][1]*(inp[1][0]*inp[2][2]-inp[2][0]*inp[1][2])
        det3 = inp[0][2]*(inp[1][0]*inp[2][1]-inp[2][0]*inp[1][1])
        oup = det1-det2+det3
    return oup