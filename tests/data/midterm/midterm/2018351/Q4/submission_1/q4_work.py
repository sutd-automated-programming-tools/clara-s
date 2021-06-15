def determinant(M):
    
    if len(M) == len(M[0]):
        
        if len(M)>=1 and len(M)<=3:
            if len(M) == 1:
                det=M[0][0]
                return det
        
            elif len(M) == 2:
                det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
                return det
        
            elif len(M) == 3:
                det_1 = int(M[1][1]*M[2][2]-M[1][2]*M[2][1])
                det_2 = int(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                det_3 = int(M[1][0]*M[2][1]-M[1][1]*M[2][0])
                det = M[0][0]*det_1-M[0][1]*(det_2)-M[0][2]*(det_3)
                return det
    else:
        return None