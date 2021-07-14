
def determinant(m):
    for item in m:
        x=len(m[0])
        if not x==len(item):
            return None
        if len(m[0])==1:
            return m[0]
        
        elif len(m[0])==3:
            det =m[0][0]*(m[1][1]*m[2][2]-m[2][1]*m[1][2])-m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
            return det
        elif len(m[0])==2:
            return m[0][0]*m[1][1]-m[1][0]*m[0][1]     