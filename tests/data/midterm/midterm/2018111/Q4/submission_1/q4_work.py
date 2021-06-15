def det_2(m):
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

def determinant(n):
    if len(n)==1:
        return n[0][0]
    elif len(n)==2:
        if len(n[0])==2 and len(n[1])==2:
            return det_2(n)
    elif len(n)==3:
        if len(n[0])==3 and len(n[1])==3 and len(n[2])==3:
            mat_1=[n[1][1:3],n[2][1:3]]
            mat_2=[[],[]]
            mat_2[0].append(n[1][0])
            mat_2[0].append(n[1][2])
            mat_2[1].append(n[2][0])
            mat_2[1].append(n[2][2])
            mat_3=[n[1][0:2],n[2][0:2]]
            return n[0][0]*det_2(mat_1)-n[0][1]*det_2(mat_2)+n[0][2]*det_2(mat_3)
    return None